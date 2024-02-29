from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.home, name='home'),
    path('terms', views.terms_of_service, name='terms_of_service'),
]