from django.template import loader
from django.http import HttpResponse, HttpRequest


def home(request: HttpRequest):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def terms(request: HttpRequest):
    template = loader.get_template('terms.html')
    return HttpResponse(template.render())
