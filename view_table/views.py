from django.shortcuts import render,HttpResponseRedirect,reverse,get_object_or_404
from django.contrib.messages import error
import logging
from .models import UxProduct,UxUser
from django.db.models import Q
from operator import itemgetter
# Create your views here.


def home(request):

    return render(request,'view_table/home.html')

def query_input(request):

    return render(request,'view_table/query_input.html')

def query_result(request):

    return render(request,'view_table/query_result.html')

def data_collection(request):

    return render(request,'view_table/data_collection.html')

def status_information(request):

    return render(request,'view_table/status_information.html')

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
    u1 = UxUser.objects.filter(nickname=request.GET["fulltext"])
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


