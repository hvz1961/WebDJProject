from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'films/index.html')

def new(request):
    return render(request, 'films/new/html')
