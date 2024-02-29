from . import views 
from django.urls import path

app_name ='home_page'

urlpatterns=[
    path('',views.home_page,name='home_page'),
]