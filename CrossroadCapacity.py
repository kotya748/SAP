print("Daniel`s CrossroadCapacity\n\n")


def print_single_crossroad(lines_horizontal, lines_vertical, crossroads_num):

    if lines_vertical == 1:
        print("      ║  ^  ║")
        print("      ║  ^  ║")
        print("══════╝  ^  ╚══════")
        if lines_horizontal == 1:
            print(" » » »       » » »")
        if lines_horizontal == 2:
            print(" » » »       » » »\n » » »       » » »")
        print("══════╗  ^  ╔══════")
        print('      ║  ^  ║')
        print('      ║  ^  ║')
    if lines_vertical == 2:
        print("      ║  ^ ^  ║")
        print("      ║  ^ ^  ║")
        print("══════╝  ^ ^  ╚══════")
        if lines_horizontal == 1:
            print(" » » »         » » »")
        if lines_horizontal == 2:
            print(" » » »         » » »\n » » »         » » »")
        print("══════╗  ^ ^  ╔══════")
        print('      ║  ^ ^  ║')
        print('      ║  ^ ^  ║')
    if crossroads_num > 0:
        crossroads_num = crossroads_num - 1
        print_single_crossroad(lines_horizontal, lines_vertical, crossroads_num)


def capacity_counter(lines_horizontal, lines_vertical, crossroads_num):
    crossroads_num += 1
    print("\n- - - - - - - - - - - - -\n")
    green_light_time = 30
    print(f"Time of green light: {green_light_time}")
    cars = int(250/4)
    print(f"Maximum cars between crossroads: {cars}")
    cross_time = 10 * (8/100)
    print(f"1 car pass crossroad in {cross_time} seconds")
    # horizontal_capacity = (30 / 0.8) * lines_horizontal * crossroads_num
    horizontal_capacity = (green_light_time / cross_time) * lines_horizontal * crossroads_num
    # vertical_capacity = (30 / 0.8) * lines_vertical * crossroads_num
    vertical_capacity = (green_light_time / cross_time) * lines_vertical * crossroads_num
    single_horizontal_capacity = horizontal_capacity / crossroads_num
    single_vertical_capacity = vertical_capacity / crossroads_num
    print(f"Vertical capacity of single crossroad: {single_vertical_capacity}")
    print(f"Horizontal capacity of single crossroad: {single_horizontal_capacity}")
    print(f"Total capacity of single crossroad: {single_vertical_capacity + single_horizontal_capacity}")
    if crossroads_num > 1:
        print(f"Total crossroads capacity: {horizontal_capacity + vertical_capacity}")



try:
    crossroads = (int(input("Number of crossroads:")) - 1)
except ValueError:
    print("Error!")
    crossroads = 0
horizont = input("Horizontal lines(1-2): ")
vertical = input("Vertical lines(1-2): ")

try:
    print_single_crossroad(int(horizont), int(vertical), crossroads)
except ValueError:
    print("Error!")
    input("Press any button to exit..")
try:
    capacity_counter(int(horizont), int(vertical), crossroads)
except ValueError:
    print("Error!")
    input("Press any button to exit..")

