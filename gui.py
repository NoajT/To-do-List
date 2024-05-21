import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do: ")
input_box = sg.InputText(tooltip="Enter To-do")
add_button = sg.Button("Add")

window = sg.Window('To-Do List', layout=[[label], [input_box, add_button]])
window.read()
window.close()
