from django.urls import path          #imports path and include function
from . import views                   #imports local views.py file 

urlpatterns = [
path('',views.index, name ='index'),  # url dispatcher, path is imported from views.py, then we reference the function index 
]