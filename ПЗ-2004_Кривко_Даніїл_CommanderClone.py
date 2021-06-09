import os
import shutil
print("Welcome to Daniel`s TerminalCommander v.alpha")
print("Type 'help' to get command list")


def user_input(text):
    return input(text)


def list_commands():
    print("Available commands:")
    commands = {
        "exit": "exit program", "ls": "list directory", "mkdir": "make directory", "rmdir": "remove an empty directory",
        "rm": "remove files", "cp": "copy files or directories", "help": "list commands",
        "path": "get current directory", "mv": "move files or directory", "cd": "change directory"
    }
    dictionary = commands.items()
    for x in dictionary:
        print(x)


def operations(input):
    if input != "exit":

        if input == "ls":
            print(os.listdir())

        elif input == "cd":
            try:
                os.chdir(user_input("Folder name:"))
            except FileNotFoundError:
                print("No such directory")
        elif input == "mkdir":
            os.mkdir(user_input("Folder name:"))
        elif input == "rmdir":
            try:
                os.rmdir(user_input("Folder name:"))
            except OSError:
                print("Directory not empty")
            except FileNotFoundError:
                print("No such directory")

        elif input == "rm":
            try:
                os.remove(user_input("File name:"))
            except FileNotFoundError:
                print("No such file")

        elif input == "cp":
            try:
                source = user_input("Source path:")
                destination = user_input("Destination path:")
                shutil.copyfile(source, destination)
            except FileNotFoundError:
                print("Error, no such file")

        elif input == "help":
            list_commands()

        elif input == "path":
            print(os.getcwd())

        elif input == "mv":
            source = user_input("Source path:")
            destination = user_input("Destination path:")
            os.replace(source, destination)
    else:
        return 0
    operations(str(user_input(">>> ")))


operations(str(user_input(">>> ")))


