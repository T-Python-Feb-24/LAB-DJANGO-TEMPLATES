from . import views
from django.urls import path

app_name = "google"

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("terms/", views.terms_page, name="terms_page"),
]