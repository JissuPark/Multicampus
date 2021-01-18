from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from todo_js_app.models import Todojs


def index(req):
    todos = Todojs.objects.all()
    return render(req, 'todo_js_app/index.html', {'db': todos})


def create_todo(req):
    _title = req.GET['todoInput']
    todo = Todojs(title=_title)
    todo.save()
    return HttpResponseRedirect(reverse('index'))


def delete_todo(req):
    _id = req.GET['todoNum']
    td = Todojs.objects.get(id=_id)
    td.delete()
    return HttpResponseRedirect(reverse('index'))


def clear_todo(req):
    todos = Todojs.objects.all()
    todos.delete()
    return HttpResponseRedirect(reverse('index'))
