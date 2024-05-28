FILEPATH = 'tasks.txt'


def get_tasks(filepath=FILEPATH):
    """ Read text file and return list of
    task items created by user.
    """
    with open(filepath, 'r') as file_local:
        tasks_local = file_local.readlines()
    return tasks_local


def write_tasks(tasks_arg, filepath=FILEPATH):
    """ Writes list of task items created by
    user to a text file.
    """
    with open(filepath, 'w') as file:
        file.writelines(tasks_arg)


if __name__ == "__main__":
    print("hello")
    print(get_tasks())
