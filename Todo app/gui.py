import functions
import PySimpleGUI as sg
import time
import os

#error handling if file not present
if not os.path.exists(r"database.txt"):
    with open(r"database.txt",'w') as file:
        pass

# initalize all the gui element
clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter todo",key= "todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete")
exit_button = sg.Button("Exit")
list_box = sg.Listbox(values = functions.get_todos(),
                      key = 'sel_todo',
                      enable_events = True,
                      size = [45,10])

# initiliaze the view of the window
window = sg.Window('My To-Do App',layout = [[clock],
                                            [label],
                                            [input_box, add_button],
                                            [list_box,edit_button, delete_button],
                                            [exit_button]])
while True:
    event, value = window.read(timeout = 10)
    window['clock'].update(value = time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            new_todo = value['todo']
            todos = functions.add_todo(new_todo)
            window['sel_todo'].update(values = todos) # update the list view
            window['todo'].update(value = '') #update the input_box
            #print(functions.get_todos())
        case 'Edit':
            try:
                if value['todo'] != '':
                    todos = functions.edit_todo(sel_todo = value['sel_todo'][0],
                                    new_todo = value['todo'])
                    window['sel_todo'].update(values = todos) #refreshes the list view with new value
            except IndexError:
                sg.popup("Please select a item first.", font = ('Helvetica', 20))
                
        case 'Delete':
            try:
                todos = functions.delete_todo(value['todo'])
                window['sel_todo'].update(values = todos)
                window['todo'].update(value = '')
            except IndexError:
                sg.popup("Please select a item first.", font = ('Helvetica', 20))
        case 'sel_todo':
            window['todo'].update(value = value['sel_todo'][0]) # update input box on selection of a todo
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break
    
window.close()    
