# coding=utf-8
import math
import cmath


def get_abc():
    tempA = input("Введите а :")
    tempB = input("Введите b :")
    tempC = input("Введите c :")
    try:
        a = int(tempA)
        b = int(tempB)
        c = int(tempC)
    except ValueError:
        try:
            a = float(tempA)
            b = float(tempB)
            c = float(tempC)
        except ValueError:
            print("ERROR!")
            exit()
    return a, b, c


# Задача 37
# Даны  действительные  числа  а,  Ь,  с.  Удвоить  эти числа,
# если a >= b >= c или заменить  их  абсолютными  значениями,  если  это  не так.
print("Задача № 37? (y/n)")
answer = input(">>> :  ")
if answer == "y":
    a, b, c = get_abc()
    if a >= b >= c:
        a, b, c = a * 2, b * 2, c * 2
        print(f"удвоенные значения: {a}, {b}, {c}\n")
    else:
        a, b, c = abs(a), abs(b), abs(c)
        print(f"Абсолютные значения: {a}, {b}, {c} \n")

# Задача 41
# 41.  Даны  три  действительных  числа.
# Выбрать  из  них те,  которые  принадлежат  интервалу  (1,  3)
print("Задача № 41? (y/n)")
answer = input(">>> :  ")
if answer == "y":
    a, b, c = get_abc()
    print("Принадлежат  интервалу  (1,  3): ")
    if 1 < a < 3:
        print(a)
    if 1 < b < 3:
        print(b)
    if 1 < c < 3:
        print(c)

# 47.  Даны  действительные  положительные  числа  х, у, z.
# а)  Выяснить,  существует  ли  треугольник  с  длинами сторон  х,  y, z.
# б)  Если  треугольник  существует,  то  ответить— является  ли  он  остроугольным
print("Задача № 47? (y/n)")
answer = input(">>> :  ")
if answer == "y":
    x, y, z = get_abc()
    if x + y > z and y + z > x and x + z >y:
        print("Треугольник со сторонами (а, б, с) существует")
        if x == y == z:
            print("треугольник является остроугольным")
        elif x < y <= z or y < x <= z or z < x <=y:
            print("треугольник является остроугольным")
        else:
            print("треугольник НЕ является остроугольным")
    else:
        print("Треугольник со сторонами (а, б, с) НЕ существует")


# 51.  Даны  действительные  числа  а,  b, с  (а != 0).
# Полностью исследовать биквадратное уравнение ах^4 +  Ьх^2 +  с = 0
# , т.е. если  действительных  корней  нет,  то  должно  быть выдано  сообщение  об  этом,
# иначе  должны  быть  выданы два  или  четыре  корня.

print("Задача № 51? (y/n)")
answer = input(">>> :  ")
if answer == "y":
    a, b, c = get_abc()
    discriminant = b*b - 4 * a * c
    if discriminant < 0:
        print(f"Discriminant - {discriminant}")
        print("действительных  корней  нет")
    elif discriminant == 0:
        print("Дискриминант равен 0..")
        y = (-b / 2*a)
        x = math.sqrt(y)
        print(f"x1 : {x}, x2 : {-x}")
    elif discriminant > 0:
        print("Дискриминант - ", discriminant)
        y1 = (-b + math.sqrt(discriminant) / 2 * a)
        print(f"y1 : {y1}")
        x1 = math.sqrt(y1)
        y2 = (-b - math.sqrt(discriminant) / 2 * a)
        print(f"y2 : {y2}")
        x2 = cmath.sqrt(y2)
        print(f"x1 : {x1}, x2 : {-x1}, x3 : {x2}, x4 : {-x2}")
