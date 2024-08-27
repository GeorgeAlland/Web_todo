import functions
import FreeSimpleGUI as sg

label = sg.Text ("Type in a ToDo")
input_box = sg.InputText(tooltip = "Enter a Todo..")
add_button =sg.Button("Add",)


window = sg.Window("My TODO App",layout=[[label], [input_box, add_button]])
window.read()
window.close()