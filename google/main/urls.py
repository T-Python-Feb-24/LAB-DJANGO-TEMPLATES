from . import views
from django.urls import path

app_name ='main'

urlpatterns = [
    path("", views.home_page , name="home_page"),
    path("terms/", views.terms_page,name="terms_page"),
]
