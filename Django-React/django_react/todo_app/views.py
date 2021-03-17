from rest_framework.decorators import api_view
from rest_framework import status
from .models import Todo
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

'''
class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
'''

# url = /
@api_view(['GET'])
def index(request):
    _all = Todo.objects.all()
    _serialize = TodoSerializer(_all, many=True)
    return Response(_serialize.data)


# url = /create_todo
@api_view(['POST'])
def create_todo(request):
    new_todo = TodoSerializer(data=request.data)
    if new_todo.is_valid():
        new_todo.save()
        _all = TodoSerializer(Todo.objects.all(), many=True)
        return Response(_all.data)
    return Response(new_todo.errors, status=status.HTTP_400_BAD_REQUEST)


# url = /delete_todo
@api_view(['DELETE'])
def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    _serialize = TodoSerializer(Todo.objects.all(), many=True)
    return Response(_serialize.data)
