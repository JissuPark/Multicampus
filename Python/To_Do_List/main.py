from controller.todo_controller import TodoController
from view_template.views import *

controller = TodoController()

controller.file_read()

while True:
    showmenu()

    _menu = menu_select()

    if _menu.isdecimal():
        
        _menu = int(_menu)

        if _menu == 1:
            _id = controller.find_next_id()
            todo = menu1(_id)
            controller.register(todo)
            
        elif _menu == 2:
            todo = menu2()
            controller.update(todo)

        elif _menu == 3:
            _id = menu3()
            controller.remove(_id)

        elif _menu == 4:
            _list = controller.showall()
            menu4(_list)

        elif _menu == 5:
            menu5()
            controller.clear()

        else:
            print('Your input must be an integer between 1 and 5')
            print('If you want to quit, press "q" or "Q"')

    elif _menu == 'q' or _menu == 'Q':
        print('Quit the program now')
        print('Thanks a lot!')
        break

    else:
        print('Your input must be an integer between 1 and 5')
        print('If you want to quit, press "q" or "Q"')

controller.file_write()