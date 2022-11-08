import math
# creating a function to calculate the number of paint that can be needed for a wall


def paint_calc(height, width, coverage):
    number_of_cans = math.ceil((height * width)/coverage)
    print(f'{number_of_cans} cans can do the work')


test_h = int(input("Enter the height of the wall: "))
test_w = int(input("Enter the width of the wall: "))
cover = 5
paint_calc(height=test_h, width=test_w, coverage=cover)
