#Given the radius of the circle, write a program to print the circumference and area of the circle. Write functions to calculate area and circumference

import math
from math import pi
def rof(radius):
        #Area of circle
     Area_circle = pi * radius ** 2
     return Area_circle
def cir(radius):
        #circumference
     circ=2*pi*radius
     return circ

def main():
    radius = float(input("Input the radius of the circle : "))
    print("Area of the circle is ", rof(radius))
    print("Circumference of the circle is:", cir(radius))
main()





