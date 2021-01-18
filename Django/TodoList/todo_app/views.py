from django.shortcuts import render, HttpResponseRedirect
from todo_app.models import Todo
from django.urls import reverse

# url = /
def index(request):
    _todos = Todo.objects.all()
    return render(request, 'todo_app/index.html', {'todos': _todos})


# url = /create_todo
def create_todo(request):
    content = request.POST['todoContent']
    new_todo = Todo(title=content)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))


# url = /delete_todo
def delete_todo(request):
    _id = request.GET['todoNum']
    todo = Todo.objects.get(id=_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))


def show_list(request):
    pass


def remove_list(request):
    pass
