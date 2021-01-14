from dao.file_dao import init_load_data, save_list

class TodoService:

    todos = []


    def file_read(self):
        TodoService.todos = init_load_data()


    def file_write(self):
        save_list(TodoService.todos)


    def addtodo(self, _todo):
        TodoService.todos.append(_todo)
        return f'"{_todo._id}"-"{_todo._title}" is added!'


    def updatetodo(self, _todo):
        for todo in TodoService.todos:
            if todo._id == _todo._id:
                prevtitle = todo._title
                todo._title = _todo._title
                return f'"{_todo._id} is updated! "{prevtitle}"->"{_todo._title}"'
        

    def removetodo(self, _id):
        for todo in TodoService.todos:
            if todo._id == _id:
                title = todo._title
                TodoService.todos.remove(todo)
                return f'"{title}" is deleted!'
        

    def gettodo(self):
        return TodoService.todos


    def deletetodo(self):
        TodoService.todos.clear()


    def findnextid(self):
        return (TodoService.todos[-1]._id+1) if TodoService.todos else 0


    def showtodo(self):
        return TodoService.todos
