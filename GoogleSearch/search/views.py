from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'search/home.html')

def terms_of_service(request):
    return render(request, 'search/terms.html')

