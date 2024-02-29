from . import views
from django.urls import path

app_name = "main"
urlpatterns = [
    path('', views.home, name="home_page"),
    path('terms', views.terms, name="terms_page"),
]
