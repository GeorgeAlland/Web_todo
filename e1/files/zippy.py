import FreeSimpleGUI as sg

label1 = sg.Text("Select Files to Compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text(" Select Destination Folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

compress_Button = sg.Button("Compress")

window = sg.Window("Zippy", layout = [[label1, input1, choose_button1],
                                      [label2, input2, choose_button2],
                                      [compress_Button]])

window.read()
window.close()

