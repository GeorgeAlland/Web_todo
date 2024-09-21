import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkGreen")

clock = sg.Text ("", key="clock")
label = sg.Text ("Type in a ToDo")
input_box = sg.InputText(tooltip = "Enter a Todo..",key ="todo")
#add_button =sg.Button(size = 10, image_source= "Add.png")
add_button =sg.Button("Add", size = 10, mouseover_colors= "LightBlue2",
                      tooltip = "Add New TODO", key="Add")
list_box = sg.Listbox(values = functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
#complete_button = sg.Button(size = 10, image_source= "Complete.png")
complete_button = sg.Button("Complete",size = 10)
exit_button = sg.Button("Exit")

#layout = [[label],[input_box, add_button],[list_box, edit_button]]

window = sg.Window("My TODO App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                    font = ("Helvetica",10))

while True:
    event, values = window.read(timeout =200)



    if event in (None, "exit, sg.win_closed"):
        break

    window["clock"].update(value=time.strftime("%d %b, %y %H %M %S"))

    match event:
        case "Add":

            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            if new_todo != "\n":
                todos.append(new_todo)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")



        case "Edit":
            try:
                todo_to_edit =values["todos"][0]
                new_todo = values["todo"]

                todos=functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")


            except IndexError:
               sg.popup("Please select an Item to Edit.", font=("Helvetica", 10), title = "error" )


        case "Complete":

            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value = "")
            except IndexError:
                sg.popup("Please select an Item to Complete.", font=("Helvetica", 15),title = "Error")


        case "Exit":
            break

        case"todos":
            window["todo"].update(value = values["todos"][0])


        case sg.WIN_CLOSED:
            break


window.close()