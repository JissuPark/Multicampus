from django.urls import path
from .views import gugulist


urlpatterns = [
    # path('', views.GuGudanListCreate.as_view()),
    path('', gugulist, name="list")
]