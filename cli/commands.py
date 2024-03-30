from app.models import Task
from app.task_manager import TaskManager


task_manager = TaskManager()


def addTask():
    print("Adding task in progress ...")

    # reading input about task
    taskName = input("\nName of Task:\n")
    taskDescription = input("\nDescription of Task:\n")
    taskPriority = input("\nTask Priority: (Low, Medium, High, Urgent)\n")
    taskStatus = input("\nTask Status: (New, In Progress, Completed)\n")
    print("\nSending to database...")

    # creating Task object
    task = Task(taskName, taskDescription, taskPriority, taskStatus)
    task_dict = task.to_dict()

    task_manager.add_task(task_dict)


def updateTask():
    taskID = input("\nEnter Task ID:\n")
    objID = task_manager.to_ObjectID(taskID)
    task_manager.update_task(objID)


def listTasks():
    print("Listing tasks...")
    task_manager.list_tasks()


def deleteTask():
    taskID = input("\nEnter Task ID:\n")
    deleteTask = input(f"\nAre you sure you want to delete {taskID}? (y/n)\n")
    if deleteTask == "y":
        # converting from string to ObjectID
        objID = task_manager.to_ObjectID(taskID)
        task_manager.delete_task(objID)
    else:
        print("\nBack to menu...")


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
    print("\nExiting Task Manager ...\n")
    exit()
