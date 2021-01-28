from django.shortcuts import render, HttpResponseRedirect
from rest_framework.decorators import api_view

from .models import Todo
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import TodoSerializer

'''
class TodoListCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoListUpdate(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
'''


class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# url = /
@api_view(['GET'])
def index(request):
    _all = Todo.objects.all()
    _serialize = TodoSerializer(_all, many=True)
    return Response(_serialize.data)


# url = /create_todo
@api_view(['POST'])
def create_todo(request):
    if request.method == 'POST':
        content = request.data['addname']
        new_todo = Todo(title=content)
        new_todo.save()
        _all = Todo.objects.all()
        _serialize = TodoSerializer(_all, many=True)
        return Response(_serialize.data)


# url = /delete_todo
@api_view(['POST'])
def delete_todo(request):
    if request.method == 'POST':
        _id = request.data['rmvnum']
        todo = Todo.objects.get(id=int(_id))
        todo.delete()
        _all = Todo.objects.all()
        _serialize = TodoSerializer(_all, many=True)
        return Response(_serialize.data)
