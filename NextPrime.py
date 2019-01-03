#Given a number, find the next prime number (if 8 is the input, the function should return 11. If 11 is input, it should return 13)

def NextPrime(b):
    while True:
        b=b+1
        for i in range(2, b):
            if b % i == 0:
                break
        else:
            return b
            break

def main():
    try:
        x = int(input("enter a number:"))
        if x>0:
            print("the next prime is: ", NextPrime(x))
        else:
            print("enter positive number")
            main()
    except ValueError:
        print("enter an integer")
        main()
main()
