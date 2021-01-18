from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('delete_todo/', views.delete_todo, name='delete_todo'),
    path('show_list', views.show_list, name='show_list'),
    path('remove_list', views.remove_list, name='remove_list')
]
