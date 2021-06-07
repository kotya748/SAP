import numpy
import numpy as np
from PIL import Image, ImageTk
import pygubu
try:
    import tkinter as tk
except:
    import Tkinter as tk
from tkinter import messagebox
import os
import cv2
from scipy import misc
from numpy import asarray, array
import random
import re
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import csv

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_IMG = os.path.join(PROJECT_PATH, "cat.jpeg")
print(PROJECT_IMG)


#Запускаем окно Tkinter:
root = tk.Tk()
root.withdraw()


# PHOTO_IMG = PhotoImage(file="currentimg.jpeg")
# Загружаем картинку:
# image = ImageTk.open(PROJECT_IMG)
image = Image.open("currentimg.jpeg")
image.save("currentimg.jpeg")
pixels = image.load()


# Создаём массив(кортеж) NumPy:
imgdata = np.asarray(image)
# Копия массива для обработки:
IMG_DATA = np.array(image)


#Функия подсчёта разрешения изменённой картинки:
def factorization(length):
    result = []
    d = 2
    while d * d <= length:
        if length % d == 0:
            result.append(d)
            length //= d
            print(d)
        else:
            d += 1
    if length != 1:
        print(length)
        result.append(length)
    print(f"Nubmer of factors: {len(result)}")


# Доп. информация о массиве/картинке:
# Получаем информацию о картинке:
print("[Image information]")
print(f"Pix array: {type(imgdata)}")
print(imgdata.shape)
print(f"mode: {image.mode}")
print(f"format: {image.format}")
print("Width: " + format(image.width))
print("Height: " + format(image.height) + "\n")


# Обрезаем картинку (для сокращения времени работы):
def resize_image(IMAGE):
    global PROJECT_IMG
    to_resize_cv_im = cv2.imread('currentimg.jpeg')
    resize_decision = input(f"Press Y to resize image:")
    if resize_decision == "Y" or resize_decision == "y":
        try:
            resize_percent = int(input("Input percent of picture left : "))
            new_height = int((to_resize_cv_im.shape[0] / 100) * resize_percent)
            new_width = int((to_resize_cv_im.shape[1] / 100) * resize_percent)
            print(f'New (hight, width ) == ({new_height, new_width})')
            resize_size = (new_height, new_width)
            print(f'Resized img`s shape: {resize_size}')
            cropped_im = cv2.resize(to_resize_cv_im, (new_height, new_width), interpolation=cv2.INTER_AREA)
        except ValueError:
            print("Input error, try again!")
            resize_image(IMAGE)

        cv2.imwrite('resized.jpeg', cropped_im)
        cv2.imshow('Cropped image', cropped_im)
        resized_image = Image.fromarray(IMAGE)
        cropped_im_arr = np.array(cropped_im)
        print(f"Cropped cv2/numpy arr size : {cropped_im.shape}")

        print("...resized!"), cropped_im.shape[2]
        print(f'Resized img info: ')
        # IMG_DATA = resized_image
        PROJECT_IMG = os.path.join(PROJECT_PATH, "resized.jpeg")
        print(f'Proj IMG : {PROJECT_IMG}')
        return np.array(resized_image)
    else:
        print("Resizing cancelled.")


# def resize_image(IMAGE):
#     # global IMAGE
#     resize = input(f"Press Y to resize image:")
#     if resize == "Y" or resize == "y":
#         print(f"img data len = {len(IMAGE)}")
#         resize_width, resize_height = factorization()
#         print(f"new width: {resize_width}, height: {resize_height}, RESIZING!")
#         IMAGE = np.reshape(IMAGE, (int(resize_width), int(resize_height)))
#         # IMAGE = image.resize((int(resize_width), int(resize_height)))
#     array = get_unique_pixels(IMAGE)
#     # array = np.reshape(array,(resize_width, resize_height))
#     print("resized!")
#     image.save("resized.jpeg")
#     PROJECT_IMG = os.path.join(PROJECT_PATH, "resized.jpeg")
#     return image, resize_height, resize_width


def get_unique_pixels(numpy_array):
    print("Getting unique pixels data from image array, please wait.")
    unique = set()
    for i in range(numpy_array.shape[0]):
        for j in range(numpy_array.shape[1]):
            y = numpy_array[i][j]
            # a, b, c = y
            # print(f"Element {y}, type {type(y), y.shape}")
            unique.add(str(y))
    print("Done!\n")
    return unique


# Функция нахождения кол-ва уникальных пикселей:
def filtration(numpy_array, pixel_example):
    global eq_pix_counter
    global unique_px_counter
    eq_pix_counter = 0
    for i in range(image.height):
        for j in range(image.width):
            temp_pix = numpy_array[i][j]
            if format(temp_pix) == format(pixel_example):
                eq_pix_counter += 1

    unique_px_counter += 1
    return eq_pix_counter


# Счётчики для обрабботки массива
eq_pix_counter = 0
unique_px_counter = 0

# Словарь уникальных пикселей
pixels_dictionary = {}


# Начало работы программы (Поиска пикселей):


axis0 = int(IMG_DATA.shape[0])
axis1 = int(IMG_DATA.shape[1])
print(f"Array shape (axis0): {axis0}")
print(f"Array shape (axis1) : {axis1}")
print(f"Array lenght: {axis0 * axis1}")
# resize_image(IMG_DATA)

# a, b = factorization(axis0 * axis1)
# print(f"a, b = {a, b}")
# print(f"IMG DATA TYPE : {type(IMG_DATA)}")
# leng = IMG_DATA.reshape(IMG_DATA, (axis1 * axis0), order='C')
# print(f"new arr len: {len(leng)}")


# unique_list = list(get_unique_pixels(IMG_DATA))
# print(f"Number of unique pixels: {len(unique_list)}")

# for i in range(image.height):
#     for j in range(image.width):
#         if unique_px_counter >= len(unique_list):
#             break
#         example = unique_list[unique_px_counter]
#         eq_pixels = filtration(IMG_DATA, example)
#         pixels_dictionary[example] = eq_pixels
#         print(f"Pixel: {example}; Total: {pixels_dictionary[example]}")
# print(f"Pixel dictionary length: {len(pixels_dictionary)}, ({len(pixels_dictionary) / ((axis0*axis1) / 100)} %) ")
# # print(pixels_dictionary)


# delete el in arr:
# print(img_data_copy)
# print(len(img_data_copy))
# img_data_copy = np.delete(img_data_copy, [0][0], 1)
# print("GAP")
# print(img_data_copy)
# print(len(img_data_copy))
# define the function callbacks



class MyApplication:
    global image

    def __init__(self):
        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('gUI.ui')

        #3: Create the widget using self.master as parent
        self.mainwindow = builder.get_object('mainwindow')

        # Connect method callbacks
        builder.connect_callbacks(self)
        #Загрузка виджетов граф. интерфейса:
        self.canvas = builder.get_object('canva')
        # self.frame5 = builder.get_object('frame5')
        self.checkbuttonR = builder.get_object('radiobuttonR')
        self.checkbuttonG = builder.get_object('radiobuttonG')
        self.checkbuttonB = builder.get_object('radiobuttonB')
        self.info_text_frame = builder.get_object('textframe')
        # Загрузка изображения в GUI:
        self.aux = Image.open(PROJECT_IMG)
        self.img = ImageTk.PhotoImage(self.aux)
        self.canvas.create_image(180, 350, image=self.img, anchor=tk.W)

    def run(self):
        self.mainwindow.mainloop()

    def on_image_button_clicked(self):
        global PROJECT_IMG
        self.canvas = self.builder.get_object('canva')
        self.aux = Image.open(PROJECT_IMG)
        self.img = ImageTk.PhotoImage(self.aux)
        self.canvas.create_image(180, 350, image=self.img, anchor=tk.W)
        # canvas.create_image(0,0, image=self.img, anchor='n')
        messagebox.showinfo('Image open', 'Image loaded!')

    def on_turn_button_clicked(self):
        imRotate = self.aux.rotate(90)
        imRotate.save(PROJECT_IMG + 'turned.jpeg')
        # self.canvas.delete(self.img)
        self.img = ImageTk.PhotoImage(imRotate)
        self.canvas.create_image(180, 350, image=self.img, anchor=tk.W)

    def on_channel_button_clicked(self):
        print("f")

    def resize_image(self):
        resize_decision = messagebox.askquestion('Resize image', 'Are you sure you want to resize the image?', icon='warning')
        global PROJECT_IMG
        to_resize_cv_im = cv2.imread(PROJECT_IMG)
        # resize_decision = input(f"Press Y to resize image:")
        # if resize_decision == "Y" or resize_decision == "y":
        if resize_decision != False:
            try:
                resize_percent = int(input("Input percent of picture left : "))
                new_height = int((to_resize_cv_im.shape[0] / 100) * resize_percent)
                new_width = int((to_resize_cv_im.shape[1] / 100) * resize_percent)
                print(f"new width: {new_width}, height: {new_height}, RESIZING!")
                resize_size = (new_height, new_width)
                print(f'Resized img`s shape: {resize_size}')
                cropped_im = cv2.resize(to_resize_cv_im, (new_height, new_width), interpolation=cv2.INTER_AREA)
                cv2.imwrite('resized.jpeg', cropped_im)
            except ValueError:
                print("Input error, try again!")
                self.resize_image()
            cropped_im_arr = np.array(cropped_im)
            resized_image = Image.fromarray(cropped_im_arr)
            print(f"Cropped cv2/numpy arr size : {cropped_im.shape}")
            print("...resized!"),
            print(f'Resized img info: {resized_image.info}')
            # IMG_DATA = resized_image
            PROJECT_IMG = os.path.join(PROJECT_PATH, "resized.jpeg")
            print(f'Proj IMG : {PROJECT_IMG}')
            messagebox.showwarning('Image open', 'Image successfully resized, now open it!')
        else:
            messagebox.showwarning("Cancel", "Grouping cancelled!")
            print("Resizing cancelled.")
        #         IMAGE = np.reshape(IMAGE, (int(new_width), int(new_height)))
        #         # IMAGE = image.resize((int(resize_width), int(resize_height)))
        # array = get_unique_pixels(IMAGE)
        # # array = np.reshape(array,(resize_width, resize_height))
        # print("resized!")
        # image.save("resized.jpeg")
        # PROJECT_IMG = os.path.join(PROJECT_PATH, "resized.jpeg")

    def on_group_button_clicked(self):
        self.resize_image()


    # define the method callbacks
    def on_quit_button_clicked(self):
        self.mainwindow.quit()


if __name__ == '__main__':
    app = MyApplication()
    app.run()
    image = Image.open(PROJECT_IMG)
    IMG_DATA = np.array(image)
    print(IMG_DATA.shape)
    unique_list = list(get_unique_pixels(IMG_DATA))
    print(f"Number of unique pixels: {len(unique_list)}")
()





