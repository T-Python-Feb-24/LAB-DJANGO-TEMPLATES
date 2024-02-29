from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home_page(request:HttpRequest):

    return render(request, "main/home_index.html")

def terms_page(request:HttpRequest):

    return render(request, "main/terms_index.html")
