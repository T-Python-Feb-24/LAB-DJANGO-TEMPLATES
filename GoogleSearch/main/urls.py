from . import views
from django.urls import path

app_name = "main"

urlpatterns = [
    path("", views.home_page, name='home_pag'),
    path("main/terms/",views.terms_page,name='terms')
]