from . import views
from django.urls import path

app_name ="main"

urlpatterns = [
    path("main/add/", views.home_page_view, name="add_main_vies"),
]