from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):
    return HttpResponse('<h1>Главная страница ART Photo</h1>')

def rooms(request):
    return HttpResponse('<h1>Залы ART Photo</h1>')

def services(request):
    return HttpResponse('<h1>Услуги ART Photo</h1>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена! <br> Борода из ваты!)</h1>')