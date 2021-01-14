class ToDo:
    
    def __init__(self, id, title):
        self._id = id
        self._title = title


    def __eq__(self, id):
        if self._id == id:
            return True
        else:
            return False
    

    def __str__(self):
        return f'ID : {self._id} => title : {self._title}'