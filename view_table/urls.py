from django.urls import path
from . import views

app_name='view_table'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('query_result/', views.query_result, name='query_result'),
    # path('upload/csv/', views.upload_csv, name='upload_csv'),
    path('view/', views.recommand_product, name='recommand_product'),
    path('trend/', views.trendView.as_view(), name='trend'),
    path('perfomance/', views.PerfomanceView.as_view(), name='perfomance'),
    
]
