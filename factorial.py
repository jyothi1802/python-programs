#Write a python program to find the factorial of given number
def factorial():
    num = int(input("Enter a Number:"))
    n = 1
    if num == 1:
        print(num)
    elif num == 0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1,num):
            n = n * i
        print("Factorial of", num, "is: ", n)

factorial()
