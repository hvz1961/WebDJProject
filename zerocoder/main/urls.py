from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='page2'),
    path('services', views.services, name='page3'),
    path('contact', views.contact, name='page4'),
    path('article_detail', views.article_detail, name='page5'),
    path('subscribe', views.subscribe, name='page6'),
]