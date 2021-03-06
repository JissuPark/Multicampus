from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('delete_todo/', views.delete_todo, name='delete_todo'),
    path('clear_todo/', views.clear_todo, name='clear_todo')
]
