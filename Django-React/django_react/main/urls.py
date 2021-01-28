from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainListCreate.as_view()),
]
