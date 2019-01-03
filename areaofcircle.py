# Write a Python program to find the area of a triangle

from math import pi
def area():
    radius = float(input('enter radius:'))
    a = pi * radius * radius
    if (radius < 0):
        print('enter positive number')
    else:
        print('area of circle:' + str(a))
area()
