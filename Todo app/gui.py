import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter todo",key= "todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete")
exit_button = sg.Button("Exit")
window = sg.Window('My To-Do App',layout = [[label],
                                            [input_box,add_button],
                                            [edit_button, delete_button ],
                                            [exit_button]])
while True:
    event, value = window.read()
    match event:
        case 'Add':
            new_todo = value['todo']
            functions.add_todo(new_todo)
            print(functions.get_todos())
        case 'Edit':
            new_todo = value['todo']
            functions.edit_todo(new_todo)
        case 'Delete':
            functions.delete_todo(value['todo'])
        case 'Exit':
            break
window.close()    
