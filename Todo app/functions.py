""" backend functionality of PYsimpleGui buttons for gui.py  file
    
"""

FILEPATH = r"D:\Python projects\Todo app\files\database.txt"

# get_todos() :- return the lines(todos ) store in database file
def get_todos(filepath=FILEPATH):
    with open(filepath,'r') as file:
            todos = file.readlines()
    return todos

# write_todo() :- write into the database file
def write_todos(todos, filepath=FILEPATH):
    with open(filepath,'w') as file:
            file.writelines(todos)

# adds a new todo into file            
def add_todo(todo):
    todos = get_todos()
    todos.append(todo + '\n')
    write_todos(todos)
    return todos

# edits the existing todo
def edit_todo(sel_todo,new_todo):
    todos = get_todos()
    index = todos.index(sel_todo)
    todos[index] = new_todo + '\n'
    write_todos(todos)
    return todos

# delete todo from the file
def delete_todo(todo):
    todos = get_todos()
    todos.pop(todos.index(todo))
    write_todos(todos)
    return todos

if __name__ == '__main__':
    todos = get_todos()
    print(todos.index('dance'))
    print(todos)
