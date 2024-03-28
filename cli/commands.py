from app.models import Task
from app.task_manager import TaskManager


def addTask():
    print("Adding task in progress ...")
    taskName = input("\nName of Task:\n")
    taskDescription = input("\nDescription of Task:\n")
    taskPriority = input("\nTask Priority: (Low, Medium, High, Urgent)\n")
    taskStatus = input("\nTask Status: (New , In Progress, Completed)\n")
    print("\nSending to database...")

    task = Task(taskName, taskDescription, taskPriority, taskStatus)
    task_dict = task.to_dict()

    task_manager = TaskManager()
    task_manager.add_task(task_dict)


def updateTask():
    taskName = input("\nInput Task Name to Update (case sensitive):\n")
    print(f"Looking for {taskName} now ...\n")
    print("Found Task\n")
    print(f"What would you like to update from {taskName}:")


def listTasks():
    print("Listing tasks...")


def deleteTask():
    taskName = input("\nWhich task would you like to delete (case sensitive):\n")
    print(f"Looking for {taskName} now")
    deleteTask = input(f"Are you sure you want to delete {taskName}? (y/n)\n")
    deleteTask = deleteTask.lower()
    if deleteTask == "y":
        print(f"Deleting task: {taskName}\n")
    else:
        print("Back to menu")


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
