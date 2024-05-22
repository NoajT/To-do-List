import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do: ")
input_box = sg.InputText(tooltip="Enter To-do", key="task")
add_button = sg.Button("Add")

window = sg.Window('To-Do List',
                   layout=[[label], [input_box, add_button]],
                   font=('Calibri', 16))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = values['task'] + "\n"
            tasks.append(new_task)
            functions.write_tasks(tasks)
        case sg.WIN_CLOSED:
            break

window.close()
