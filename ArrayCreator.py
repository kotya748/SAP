import os
import random
import time
import string
from PyQt5 import QtWidgets


# Функция выбора размера массива
def choose_array_size():
    # Создаю кортеж возможных размеров массива:
    array_size = (10, 100, 1000, 10_000, 1_000_000_000, 10_000_000_000)
    print("Available array size: 1)10, 2)100, 3)1000, 4)10_000, 5)1_000_000_000, 6)10_000_000_000")
    # Создаю переменную choice для выбора размера массива, создаю исключение ValueError:
    try:
        choice = input("Choose size of an array(1-6):")
        choice = int(choice) - 1
    except ValueError:
        print("Error!")
        choose_array_size()
    size = array_size[choice]
    return size


def fill_array(choice, array_size):
    def mixed(mix_choice):
        if mix_choice == 1:
            return random.randint(1, 100)
        if mix_choice == 2:
            return random.random()
        if mix_choice == 3:
            return array.append(random.choice(string.ascii_letters))
    array = list()
    if choice == 1:
        print("Generating random int array..")
        for i in range(array_size):
            array.append(random.randint(1, 100))
        print(f"Random int array: \n {array}")

    if choice == 2:
        print("Generating random float array")
        for i in range(array_size):
            array.append(random.random())
        print(f"Random float array: \n {array}")
    if choice == 3:
        print("Generating random char array")
        for i in range(array_size):
            array.append(random.choice(string.ascii_letters))
        print(f"Random char array: \n {array}")
    if choice == 4:
        print("Generating random mixed array..")
        for i in range(array_size):
            mixed_choice = random.randint(1, 3)
            array.append(mixed(mixed_choice))
        print(f"Random mixed array: \n {array}")


print("Array type: ")
choice = input("1 - int, 2 - float, 3 - char, 4 - mixed: ")
try:
    fill_array(int(choice), choose_array_size())
except ValueError:
    print("Error!")

# def choose_array_type():
#
#     choice = 0
#     print("Available array types: 1)Integers 2)Float numbers 3)Characters 4) Mixed")
#     try:
#         choice = input("Choose type of an array(1-4): ")
#         choice = int(choice)
#     except ValueError:
#         print("Error!")
#         choose_array_type()
#     if choice == 1 or choice == 2 or choice == 3 or choice == 4:
#         a = choice
#         return a
#     else:
#         print("Error, try again! \n")
#         choose_array_type()
#
#     # if choice == 1:
#     #     return random_int_list
#     # elif choice == 2:
#     #     return random_float_list
#     # elif choice == 3:
#     #     return random_char_list
#     # elif choice == 4:
#     #     return random_mixed_list
#     # else:
#     #     print("Error, try again! \n")
#     #     choose_array_type()
#
# # Создаю массивы для заполнения:
#     random_mixed_list = list()
#     random_float_list = list()
#     random_char_list = list()
#     random_int_list = list()  # random.sample(range(1, 100), array_size[0])
#
#
# print(choose_array_type())
# print("(:")

