from django.shortcuts import render
from rest_framework import generics
from .models import GuGudan
from .serializers import GuGudanSerializer


class GuGudanListCreate(generics.ListCreateAPIView):
    queryset = GuGudan.objects.all()
    serializer_class = GuGudanSerializer
