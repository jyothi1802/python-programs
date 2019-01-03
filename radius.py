#Given the area of the circle, write a program to print the radius

import math
def radius(area):
    rad=math.sqrt(area/3.14)
    return rad
def main():
    try:
        a= int(input("enter the area:"))
        if a > 0:
            print("the radius is :", radius(a))
        else:
            print("enter a positive number")
            main()
    except ValueError:
        print("enter a valid number")
        main()

main()
