import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do: ")
input_box = sg.InputText(tooltip="Enter To-do", key="task")
add_button = sg.Button("Add")
task_list_box = sg.Listbox(values=functions.get_tasks(), key='tasks',
                           enable_events=True, size=[43, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('To-Do List',
                   layout=[[label],
                           [input_box, add_button],
                           [task_list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('calibri', 16))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['tasks'])
    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = values['task'] + '\n'
            tasks.append(new_task)
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)

        case "Edit":
            task_to_edit = values['tasks'][0]
            new_task = values['task']

            tasks = functions.get_tasks()
            index = tasks.index(task_to_edit)
            tasks[index] = new_task
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)
        case "Complete":
            task_to_complete = values['tasks'][0]
            tasks = functions.get_tasks()
            tasks.remove(task_to_complete)
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)
            window['task'].update(value='')
        case "Exit":
            break
        case "tasks":
            window['task'].update(value=values['tasks'][0])
        case sg.WIN_CLOSED:
            break

window.close()
