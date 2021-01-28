from django.urls import path
from . import views


urlpatterns = [
    path('', views.std_list_create),
    path('<int:pk>/', views.std_details)
]
