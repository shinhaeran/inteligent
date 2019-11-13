from django.shortcuts import render,HttpResponseRedirect,reverse,get_object_or_404
from django.contrib.messages import error
import logging
from .models import UxProduct,UxUser,RecommendedItem,DataItem,UxProduct, Topk, TrendResult
from django.db.models import Q
from operator import itemgetter

from django.views.generic.edit import CreateView 
from django.views.generic import TemplateView,ListView

# from .forms import CreateUserForm

# Create your views here.


def home(request):

    return render(request,'view_table/home.html')

# class CreateUserView(CreateView): # generic view중에 CreateView를 상속받는다.
#     template_name = 'registration/signup.html' # 템플릿은?
#     # form_class =  CreateUserForm # 푸슨 폼 사용? >> 내장 회원가입 폼을 커스터마지징 한 것을 사용하는 경우
#     # form_class = UserCreationForm >> 내장 회원가입 폼 사용하는 경우
#     success_url = reverse_lazy('create_user_done') # 성공하면 어디로?

class RegisteredView(TemplateView): # generic view중에 TemplateView를 상속받는다.
    template_name = 'registration/signup_done.html' # 템플릿은?
    
class trendView(TemplateView): # generic view중에 TemplateView를 상속받는다.
    template_name = 'view_table/trend.html' # 템플릿은?
    def get_context_data(self, **kwargs):
        ctx =  super(trendView, self).get_context_data(**kwargs)
        # ctx['qna_form'] = QnaForm(initial={'post_pk':self.kwargs['pk']})
        topks = Topk.objects.all()
        ctx['rank1'] = topks[0]
        ctx['rank2'] = topks[1]
        ctx['rank3'] = topks[2]
        ctx['trend_result'] = TrendResult.objects.get(time=1)
        ctx['hot_topic'] = topks
        # print(ctx)
        return ctx

class PerfomanceView(TemplateView): # generic view중에 TemplateView를 상속받는다.
    template_name = 'view_table/perfomance.html' # 템플릿은?

def query_result(request):
    userID = "ObjectID(49)"
    
    recommend_product = RecommendedItem.objects.filter(uid=userID) #이름만 들어있음 product
    used_product = DataItem.objects.filter(uid="ObjectID(49)") #p.id로 접근
    used_p = list()
    used_p_name = list()
    for p in used_product:
        obj = UxProduct.objects.get(id=p.pid)
        used_p.append(obj) 
        used_p_name.append(obj.productname)
    recommend_product = list(recommend_product)
    recommend_total = recommend_product[:]
    for p in recommend_product:
        if p.product in used_p_name:
            recommend_total.remove(p)
    result = list()
    for r in recommend_total:
        print(r.product)
        result.append(UxProduct.objects.filter(productname=r.product)[0])
    
    
    return render(request,'view_table/query_result.html',{'recommend_product':recommend_product, 'used_product':used_p, 'recommmend_total1':result[0], 'recommmend_total2':result[1], 'recommmend_total3':result[2]})


def upload_csv(request):
    data = {}
    count = 0
    if "GET" == request.method:
        return render(request, "view_table/data_collection.html", data)
    # if not GET, then proceed
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse("view_table:home"))
        #if file is too large, return
        if csv_file.multiple_chunks():
            error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
            return HttpResponseRedirect(reverse("view_table:query_input"))

        file_data = csv_file.read().decode("utf-8")		

        lines = file_data.split("\n")
        print(lines)
        lines.remove('')
        
		#loop over the lines and save them in db. If error , store as string and then display
        for line in lines:						
            fields = line.split(",")
            data_dict = {}
            data_dict["name"] = fields[0]
            data_dict["start_date_time"] = fields[1]
            data_dict["end_date_time"] = fields[2]
            print(fields[0])# data_dict["notes"] = fields[3]
            count+=1
        return render(request,'view_table/status_information.html',{'count':count-1})
            # try:
            #     form = EventsForm(data_dict)
            #     if form.is_valid():
            #         form.save()					
            #     else:
            #         logging.getLogger("error_logger").error(form.errors.as_json())												
            # except Exception as e:
            #     logging.getLogger("error_logger").error(repr(e))					
            #     pass

    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
        error(request,"Unable to upload file. "+repr(e))

    return HttpResponseRedirect(reverse("view_table:query_input"))


def recommand_product(request): #user에 따라
    u1 = UxUser.objects.filter(nickname=request.GET["fulltext"]) #사용자
    product = list()
    product_dict = dict()
    for instance in u1:
        product = UxProduct.objects.all().filter(Q(skintype=instance.skintype)|Q(gender=instance.gender)|Q(job=instance.job))[:100]
        for i,p in enumerate(product):
            stack = 0
            if(p.skintype == instance.skintype):
                stack+=1
            if(p.gender == instance.gender):
                stack+=1
            if(p.job == instance.job):
                stack+=1
            # print(i,p.productname)
            product_dict.update({p.productname:stack})
            
    
    sdict=sorted(product_dict.items(),key=itemgetter(1),reverse=True)
    print('dict:',sdict)
    # product = UxProduct.objects.filter(brandname='라네즈')
    # print(product)
   
    # user = get_object_or_404(UxUser,field_id='ObjectId(5a9cf3b1a5440e033633f766)')
    # print(user.nickname)
    # for p in product:
    #     if(p.skintype==user.skintype):
    #         print('와!')

  
    return render(request,'view_table/query_result.html',{'product':product,})


