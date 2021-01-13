import os
todos = []

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


def selectment():
    while True:
        _menu = input('Choose what you want to do : ')
        if _menu.isdecimal():
            _menu = int(_menu)
            if _menu == 1:
                menu1()
                continue
            elif _menu == 2:
                menu2()
                continue
            elif _menu == 3:
                menu3()
                continue
            elif _menu == 4:
                menu4()
                continue
            elif _menu == 5:
                menu5()
                continue
            else:
                print('Your input must be an integer between 1 and 5')
                print('If you want to quit, press "q" or "Q"')
                continue

        elif _menu == 'q' or _menu == 'Q':
            return -1
        
        else:
            print('Your input must be an integer between 1 and 5')
            print('If you want to quit, press "q" or "Q"')
            continue


def findnextid():
    return (todos[-1]['id']+1) if todos else 0


def menu1():
    print('='*50)
    print('[ADD menu]')
    print('-'*40)
    _id = findnextid()
    print(f'ID for register : {_id}')
    _title = input('Insert Something to do : ')
    addtodo(_id, _title)
    print('[COMPLETE] add to list!')
    print('='*50)
    print()


def menu2():
    print('='*50)
    print('[UPDATE menu]')
    print('-'*40)
    while True:
        _id = input('Insert ID you want to update :')
        if _id.isdecimal():
            print(f'ID for register : {_id}')
            _id = int(_id)
            _title = input('Insert Something to change : ')
            updatetodo(_id, _title)
            print('[COMPLETE] update to list!')
            break
        else:
            continue
    print('='*50)
    print()


def menu3():
    print('='*50)
    print('[REMOVE menu]')
    print('-'*40)
    while True:
        _id = input('Insert ID you want to remove : ')
        if _id.isdecimal():
            _id = int(_id)
            removetodo(_id)
            print('[COMPLETE] remove to list!')
            break
        else:
            continue
    print('='*50)
    print()


def menu4():
    print('='*50)
    print('[SHOW menu]')
    print('-'*40)
    showtodo()
    print('[COMPLETE] show to list!')
    print('='*50)
    print()


def menu5():
    print('='*50)
    print('[DELETE menu]')
    print('-'*40)
    deletetodo()
    print('[COMPLETE] delete to list!')
    print('='*50)
    print()


def addtodo(_id, _title):
    newtodo = {'id':_id, 'title': _title}
    todos.append(newtodo)


def updatetodo(_id, _title):
    for todo in todos:
        if todo['id'] == _id:
            todo['title'] = _title
            break
    

def removetodo(_id):
    for todo in todos:
        if todo['id'] == _id:
            todos.remove(todo)
            break
    

def showtodo():
    for todo in todos:
        print(f'ID : {todo["id"]}, title : {todo["title"]}')


def deletetodo():
    todos.clear()


def loaddata():
    _path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(_path)
    print(_path)
    if os.path.exists('todos.dat'):
        fd = open(_path+'\\todos.dat', 'r')
        context = fd.readlines()
        for line in context:
            _id, _title = line.split(',')
            todos.append({'id': int(_id), 'title': _title.strip()})
        fd.close()
        

def savedata():
    fd = open('todos.dat', 'w')
    for todo in todos:
        fd.write(str(todo['id'])+', '+todo["title"]+'\n')
    fd.close()
        

if __name__ == "__main__":
    loaddata()
    while True:
        showmenu()
        if selectment():
            break
    savedata()