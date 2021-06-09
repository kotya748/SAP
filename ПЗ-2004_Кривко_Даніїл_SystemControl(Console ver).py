import platform
import os
import time
# import threading
# import asyncio
# from threading import Thread

print("Daniel`s SytemConrol v. alpha")
system = platform.system()
print("System:", system)

# event = threading.Event()


def delay():
    if check_user_input(input("Want to delay your command? (1   -   Yes | 2   -   No)")) == 1:
        print("Input action delay(seconds):")
        seconds = check_user_input(user_input())
        print("Your action will be delayed for", seconds, "seconds.")
        try:
            for x in range(seconds):
                time.sleep(1)
        except KeyboardInterrupt:
            exit_program()
    else:
        return


def user_input():
    return input()


def exit_program():
    print("Exit program? (1 - Yes. 2 - No):")
    a = check_user_input(user_input())
    if a == 1:
        return 0
    if a == 2:
        main()


def check_user_input(input):
    try:
        # convert to int
        val = int(input)
        return val
    except ValueError:
        try:
            # convert to float
            val = float(input)
            return val
        except ValueError:
            print("Error! Wrong input type!")
            check_user_input(user_input())


def list_commands():
    print("Available actions:")
    print("1 - Shut Down")
    print("2 - Restart")
    print("3 - Sleep")
    print("4 - Log Out")
    print("5 - Exit Program")
    print("0 - Help")
    print("Choose your action: (0 - Help)")
    system_control_linux(check_user_input(user_input()))


def system_control_windows(decision):
    if decision == 0:
         list_commands()
    elif decision == 1:
        delay()
        os.system("shutdown /p")
    elif decision == 2:
        delay()
        os.system("shutdown /r")
    elif decision == 3:
        delay()
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif decision == 4:
        delay()
        os.system("shutdown /l")
    elif decision == 5:
        exit_program()
    else:
         print("Помилка, оберіть необхідну дію(0-5):")
         system_control_windows(check_user_input(user_input()))


def system_control_linux(decision):
    if decision == 0:
         list_commands()
    elif decision == 1:
        delay()
        os.system("systemctl poweroff")
        exit_program()
    elif decision == 2:
        delay()
        os.system("firefox")
        # os.system("systemctl reboot")
        exit_program()
    elif decision == 3:
        delay()
        os.system("systemctl suspend")
        exit_program()
    elif decision == 4:
        delay()
        os.system("")
        exit_program()
    elif decision == 5:
         exit_program()
    else:
         print("Помилка, оберіть необхідну дію(0-5):")
         system_control_linux(check_user_input(user_input()))


def main():
    print("Choose your action: (0 - Help)")
    # if "Linux" in system:
    if "Linux" in system:
        system_control_linux(check_user_input(user_input()))
    elif "Windows" in system:
        system_control_windows(check_user_input(user_input()))
main()















