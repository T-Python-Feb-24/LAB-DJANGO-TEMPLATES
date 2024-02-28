from . import views
from  django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('terms/', views.term_page, name='term_page'),
    path('GoogleTerms/', views.google_term_page, name='google_term_page'),
]