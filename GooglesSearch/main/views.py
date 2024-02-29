from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

#usage

# Create your views here.
def Google_page(request:HttpRequest):
    return render(request,"main/home_page.html")

def terms_page(request:HttpRequest):
    return render(request,"main/terms.html")