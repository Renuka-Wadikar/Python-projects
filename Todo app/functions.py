FILEPATH = r"D:\Python projects\Todo app\files\database.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath,'r') as file:
            todos = file.readlines()
    return todos

def write_todos(todos, filepath=FILEPATH):
    with open(filepath,'w') as file:
            file.writelines(todos)
            
def add_todo(todo):
    todos = get_todos()
    todos.append(todo + '/n')
    write_todos(todos)


def edit_todo(todo):
    todos = get_todos()
    index = todos.index(todo)
    return index

def delete_todo(todo):
    todos = get_todos()
    todos.pop(todos.index(todo))
    write_todos(todos)


