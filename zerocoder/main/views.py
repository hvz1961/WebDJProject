from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    data = {
        'caption':'КофеЛавка'
    }
    return render(request, 'main/index.html', data)

def new(request):
    return render(request, 'main/new.html')
