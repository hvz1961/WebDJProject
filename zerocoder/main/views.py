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
def services(request):
    return render(request, 'main/services.html')
def contact(request):
    return render(request, 'main/contact.html')
def article_detail(request):
    return render(request, 'main/article_detail.html')
def subscribe(request):
    return render(request, 'main/subscribe.html')
def terms(request):
    return render(request, 'main/terms.html')
def privacy_policy(request):
    return render(request, 'main/privacy_policy.html')
