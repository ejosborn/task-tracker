def addTask():
    print("Add a Task")


def updateTask():
    print("Update a task")


def listTasks():
    print("Listing tasks...")


def deleteTask():
    print("Delete a task")


def helpCommand():
    # lists of commands
    commands_dict = {
        "help": "Displays Commands",
        "add": "Add a task to the list",
        "update": "Update a task",
        "list": "List all of your tasks",
        "delete": "Delete a task from the list",
        "exit": "Exit the program",
    }
    print("Here are the commands you can use:")

    for key, value in commands_dict.items():
        print(f"{key}\t -    {value}")


def exitCommand():
    print("Exiting Task Manager ...\n")
    exit()
