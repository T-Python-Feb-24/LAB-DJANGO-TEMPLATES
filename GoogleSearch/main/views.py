from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def home(request: HttpRequest):
 return render(request,"main/home.html")

def term(request: HttpRequest):
 return render(request,"main/terms.html")

def style(request: HttpRequest):
 return render(request,"main/style.html")