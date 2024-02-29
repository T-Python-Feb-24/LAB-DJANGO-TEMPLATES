from.import views
from django.urls import path

app_name="main"
urlpatterns=[
    path("",views.Google_page,name="Google_page"),
    path('/terms/',views.terms_page,name="terms_page")
]