from service.todo_service import TodoService
from view_template.views import printmsg


class TodoController:
    
    def file_read(self):
        service = TodoService()
        service.file_read()


    def file_write(self):
        service = TodoService()
        service.file_write()


    def find_next_id(self):
        service = TodoService()
        _id = service.findnextid()
        return _id
    
    
    def register(self, todo):
        service = TodoService()
        msg = service.addtodo(todo)
        printmsg(msg)


    def update(self, todo):
        service = TodoService()
        msg = service.updatetodo(todo)
        printmsg(msg)

    
    def remove(self, id):
        service = TodoService()
        msg = service.removetodo(id)
        printmsg(msg)


    def showall(self):
        service = TodoService()
        return service.showtodo()

    def clear(self):
        service = TodoService()
        service.deletetodo()