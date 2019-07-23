from django.urls import path
from . import views

app_name='view_table'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('query_result/', views.query_result, name='query_result'),
    path('query_Input/', views.query_input, name='query_input'),
    path('data_collection/', views.data_collection, name='data_collection'),
    path('status_information/', views.status_information, name='status_information'),
    # url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
    path('upload/csv/', views.upload_csv, name='upload_csv'),
    path('view/', views.recommand_product, name='recommand_product'),
]
