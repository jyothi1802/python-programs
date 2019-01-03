#Write a Python program to swap two variables

def swap():
    a = int(input("enter a value:"))
    b = int(input("enter b value:"))
       #Before swap
    print("\nBefore swap a = %d and b = %d" % (a, b))
    a, b = b, a
       #After swap
    print("\nAfter swaping a = %d and b = %d" % (a, b))
    
swap()
