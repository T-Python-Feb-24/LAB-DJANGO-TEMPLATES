from django.shortcuts import render, resolve_url
from django.http import HttpRequest, HttpResponse


# Create your views here.

def google_home_page(request:HttpRequest):
    return render(request, 'google_main/index.html')

def google_terms(request:HttpRequest):
    return render(request, 'google_main/terms.html')