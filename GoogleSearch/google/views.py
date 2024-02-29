from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def main_page(request:HttpRequest):

    return render(request,'google/main_page.html')

def terms_page(request:HttpRequest):

    return render(request,'google/terms_page.html')


