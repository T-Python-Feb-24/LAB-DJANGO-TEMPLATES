from django.shortcuts import render, resolve_url
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_page(request:HttpRequest):

    url_term = resolve_url('main:home_page')
    print(url_term)
    return render(request, 'main/home.html')

def term_page(request:HttpRequest):

    url_term = resolve_url('main:term_page')
    print(url_term)
    return render(request, 'main/term.html')