from django.shortcuts import render
from .models import Main
from .serializers import MainSerializer
from rest_framework import generics  # 제네릭api뷰를 위해서


class MainListCreate(generics.ListCreateAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer

