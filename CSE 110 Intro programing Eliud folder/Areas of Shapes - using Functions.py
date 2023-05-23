#Areas of Shapes - using Functions
#Author: josé Quemba4
print ()

import math

def compute_area_square (length):
    calcule = length * length
    return calcule

def compute_area_rectangle (length, width):
    calcule = length * width
    return calcule

def compute_area_circle (radius):
    calcule = math.pi*(radius)**2
    return calcule

def compute_area (usershape, value1, value2 = 1):
    calcule = -1
    if usershape == "SQUARE":
        calcule = compute_area_square (value1)
    elif usershape == "CIRCLE":
        calcule = compute_area_circle (value1)
    elif usershape == "RECTANGLE":
        calcule = compute_area_rectangle (value1, value2)
    return calcule


user_shape = ""

while user_shape != "QUIT":
    user_shape = input ('What kind of shape do you have? ')

    if user_shape.upper () == "SQUARE":
        Square_length = float(input('What is the leangth of a side of a square? '))
        area = compute_area (user_shape.upper (), Square_length)
        print (area)

    elif user_shape.upper () == "RECTANGLE":
        Rectangle_Length = float(input('What is the length of rectangle? '))
        Rectangle_Width = float(input('What is the width of the rectangle? '))
        area = compute_area (user_shape.upper (), Rectangle_Length, Rectangle_Width)
        print (area)

    elif user_shape.upper () == "CIRCLE":
        Circle_radius = float(input('What is the radius of the circle? '))
        area = compute_area (user_shape.upper (), Circle_radius)
        print (round(area, 2))




