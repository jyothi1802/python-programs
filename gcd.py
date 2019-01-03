#write a python program to find gcd of two given numbers
#gcd is greatest common divisor
def gcd(a,b):
    if (b == 0):
        print('the gcd of two numbers:',a)
    else:
        return gcd(b,a%b)


d1 = int(input("Enter a number:"))
d2 = int(input("Enter another number"))
gcd(d1, d2)


