from .views import google_terms, google_home_page
from django.urls import path 

App_name = 'google_main'

urlpatterns = [
    path('', google_home_page, name="google_home_page"),
    path('terms/', google_terms, name="google_terms")
]