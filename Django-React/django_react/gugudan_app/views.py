from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import GuGudan
from .serializers import GuGudanSerializer


class GuGudanListCreate(generics.ListCreateAPIView):
    queryset = GuGudan.objects.all()
    serializer_class = GuGudanSerializer

@api_view(["GET"])
def gugulist(req):
    _all = GuGudan.objects.all()
    _serialize = GuGudanSerializer(_all, many=True)
    return Response(_serialize.data)