from django.urls import path
from .import views

urlpatterns = [
    path('', views.new, name='films'),
    path('index/', views.index, name='add_film'),
    # path('', views.index, name='add_film'),
    # path('new/', views.new, name='films'),

]
