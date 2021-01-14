from os import path, chdir
from entity.todo import ToDo


def save_list(todos):
    _path = path.dirname(path.realpath(__file__))
    chdir(_path)
    with open('todos.dat', 'w') as file:
        for index, todo in enumerate(todos):
            file.write(f"{index} | {todo._id}, {todo._title}\n")

def init_load_data():
    _path = path.dirname(path.realpath(__file__))
    chdir(_path)
    todos = []
    datfile = path.isfile('todos.dat')
    if datfile:
        with open('todos.dat') as rfile:
            context = rfile.readlines()
            for line in context:
                todo = line.split('|')[1].strip().split(',')
                todos.append(ToDo(int(todo[0]), todo[1]))
    return todos