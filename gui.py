import functions
import FreeSimpleGUI as fSg
import time

fSg.theme("DarkBlue14")

clock = fSg.Text('', key="Clock")
label = fSg.Text("Type in a To-Do: ")
input_box = fSg.InputText(tooltip="Enter To-do", key="task")
add_button = fSg.Button("Add")
task_list_box = fSg.Listbox(values=functions.get_tasks(), key='tasks',
                            enable_events=True, size=(43, 10))
edit_button = fSg.Button("Edit")
complete_button = fSg.Button("Complete")
exit_button = fSg.Button("Exit")

window = fSg.Window('To-Do List',
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [task_list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 16))
while True:
    event, values = window.read(timeout=200)
    window["Clock"].update(value=time.strftime("%B %d, %Y %I:%M %p"))
    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = values['task'] + '\n'
            tasks.append(new_task)
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)

        case "Edit":
            try:
                task_to_edit = values['tasks'][0]
                new_task = values['task']

                tasks = functions.get_tasks()
                index = tasks.index(task_to_edit)
                tasks[index] = new_task
                functions.write_tasks(tasks)
                window['tasks'].update(values=tasks)
            except IndexError:
                fSg.popup("Please select an item first.", font=('Helvetica', 16))
        case "Complete":
            try:
                task_to_complete = values['tasks'][0]
                tasks = functions.get_tasks()
                tasks.remove(task_to_complete)
                functions.write_tasks(tasks)
                window['tasks'].update(values=tasks)
                window['task'].update(value='')
            except IndexError:
                fSg.popup("Please select an item first.", font=('Helvetica', 16))
        case "Exit":
            break
        case "tasks":
            window['task'].update(value=values['tasks'][0])
        case fSg.WIN_CLOSED:
            break

window.close()
