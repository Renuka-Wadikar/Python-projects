import time
from functions import get_todos , write_todos

now = time.strftime("%b %d, %Y  %H:%M:%S")
print("Hello!! It is " +  now)
user_prompt = "Type add,show,edit,delete or exit\n"
            
while True:
    user_action = input(user_prompt).lower().strip() 
    todos = get_todos()   
    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos.append(todo)
        
        write_todos(todos=todos)
        
    elif user_action.startswith('show'):
        for index,item in enumerate(todos):
            print("{} - {}".format(index+1,item.title()) , end= '')
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[4:].strip())
            todos[number-1] = input("Edit this item as: \n") + "\n"
            write_todos(todos=todos)
        except:   
            print("Wrong command, Kindly enter the index of todo to edit")
    
    elif user_action.startswith('delete'):
        number = int(input("Enter the number of item to delete: "))
        todos.pop(number-1)
        write_todos(todos=todos)
    elif 'exit' in user_action:
        break
    else:
        print('Please enter a valid command!!')

print("Bye!!")