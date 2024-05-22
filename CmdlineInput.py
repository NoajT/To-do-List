import functions
import time


print("It is", time.strftime("%B %d, %Y %I:%M %p"))


while True:
    # Get user input and strip "space" characters from it
    User_action = input("Type Add, Show, Edit, Complete, or Exit: ")
    User_action = User_action.strip()

    if User_action.startswith("add"):
        task = User_action[4:] + '\n'

        tasks = functions.get_tasks()

        tasks.append(task)

        functions.write_tasks(tasks)

    elif User_action.startswith("show"):
        tasks = functions.get_tasks()

        for index, item in enumerate(tasks):
            item = item.strip('\n')
            row = f"{index + 1}: {item}"
            print(row.title())
    elif User_action.startswith("edit"):
        try:
            number = int(User_action[5:])
            print(number)

            number = number - 1

            tasks = functions.get_tasks()

            new_task = input("What should it be instead?: ")

            tasks[number] = new_task + '\n'

            functions.write_tasks(tasks)

        except ValueError:
            print("Your command is not valid.")
            print("The format for edit must be 'edit (number of the task you want to edit).")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue

    elif User_action.startswith("complete"):
        try:
            number = int(User_action[9:])

            tasks = functions.get_tasks()
            index = number - 1
            task_done = tasks[index].strip('\n')
            tasks.pop(index)

            functions.write_tasks(tasks)

            message = f"{task_done.title()} all done? Great job!"
            print(message)
        except ValueError:
            print("Your command is not valid.")
            print("The format for complete must be 'complete (number of the task you want to mark as done).")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue

    elif User_action.startswith("exit"):
        break
    else:
        print("This command is not valid. Please try again.")

print("Buh-bye now~!")
