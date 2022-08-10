from django.urls import path          #imports path and include function
from . import views                   #imports local views.py file 

urlpatterns = [
#path('',views.index, name ='index'),  # url dispatcher, path is imported from views.py, then we reference the function index 
path('', views.index,{'pagename':''}, name='home'), #gets called  after anything passed to this function
path('<str:pagename>', views.index, name='index'), #capture everything after domain name and send to view as string
]