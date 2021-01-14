from entity.todo import ToDo

def showmenu():
    print('='*50)
    print('[Today To Do List]')
    print('-'*40)
    print('menu')
    print('1. ADD something to do')
    print('2. UPDATE by ID')
    print('3. REMOVE by ID')
    print('4. SHOW list')
    print('5. DELETE all')
    print('='*50)
    print()


def menu_select():
    _menu = input('Choose what you want to do : ')
    return _menu


def menu1(_id):
    print('='*50)
    print('[ADD menu]')
    print('-'*40)
    print(f'ID for register : {_id}')
    _title = input('Insert Something to do : ')
    print('='*50)
    print()
    return ToDo(_id,_title)


def menu2():
    _id = 0
    _title = ''
    print('='*50)
    print('[UPDATE menu]')
    print('-'*40)
    while True:
        _id = input('Insert ID you want to update :')
        if _id.isdecimal():
            print(f'ID for update : {_id}')
            _id = int(_id)
            _title = input('Insert Something to change : ')
            break
        else:
            print('[WARNING] ID must be an integer!')
            continue
    print('='*50)
    print()
    return ToDo(_id,_title)

def menu3():
    _id = 0
    print('='*50)
    print('[REMOVE menu]')
    print('-'*40)
    while True:
        _id = input('Insert ID you want to remove : ')
        if _id.isdecimal():
            _id = int(_id)
            break
        else:
            print('[WARNING] ID must be an integer!')
            continue
    print('='*50)
    print()
    return _id

def menu4(_list):
    print('='*50)
    print('[SHOW menu]')
    print('-'*40)
    showlist(_list)
    print('[COMPLETE] show to list!')
    print('='*50)
    print()


def menu5():
    print('='*50)
    print('[DELETE menu]')
    print('-'*40)
    print('[COMPLETE] delete to list!')
    print('='*50)
    print()


def printmsg(msg):
    print(f'[COMPLETE] {msg}')


def showlist(todos):
    for todo in todos:
        print(f'ID : {todo._id}, title : {todo._title}')

