from django.shortcuts import render, redirect
from .models import Films_post
from .forms import Films_postForm
from django.http import HttpResponse

def new(request):
    reviews = Films_post.objects.all()
    return render(request, 'films/new.html', {'reviews': reviews})

def index(request):
    error = ''
    if request.method == 'POST':
        form = Films_postForm(request.POST)  # Сюда сохранится информация от пользователя.
        if form.is_valid():
            form.save()
            return redirect('films')
        else:
            error = "Данные были заполнены некорректно"

    form = Films_postForm()
    return render(request,'films/index.html', {'form': form, 'error': error})

