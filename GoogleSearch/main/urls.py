from . import views
from  django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('terms/', views.term_page, name='term_page'),
]