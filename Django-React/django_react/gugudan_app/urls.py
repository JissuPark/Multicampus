from django.urls import path
from . import views


urlpatterns = [
    path('', views.GuGudanListCreate.as_view()),
]