#Write a python program to check whether given number is even or odd
def oddeven():
    n = int(input('enter a number:'))
    if(n<0):
        print("enter positive num")
    elif (n % 2 == 0):
        print('even')
    else:
        print('odd')

oddeven()
