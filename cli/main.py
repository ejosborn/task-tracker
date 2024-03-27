from commands import addTask, updateTask, exitCommand, deleteTask, helpCommand

commands = {
    "add": addTask,
    "update": updateTask,
    "delete": deleteTask,
    "help": helpCommand,
    "exit": exitCommand,
}


def main():
    print("\n--------- Welcome to your Task Manager System ---------\n")
    print("Type Help to get a list of commands")
    helpHint = 0
    while True:
        command = input("\nTMS > ")
        command = command.lower()

        # if command == "exit":
        #     print("Exiting Task Manager ...\n")
        #     exitCommand()

        # if command == "help":
        #     helpCommand()

        if command in commands:
            commands[command]()
        else:
            if helpHint == 2:
                print("Command Unknown, use command *Help* for more options")
                helpHint = 0
            else:
                print("Command Unknown")
                helpHint += 1


main()
