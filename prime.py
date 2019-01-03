#Write a python program to check whether given number is prime or not
def find_prime():
    try:
        num = int(input("Enter a Number:"))
        if(num>0):

            for i in range(2,num//2+1) :
                    if (num % i == 0):
                        print(b,"is not prime")
                        break
            else:

                return num
        else:
            print("Enter positive number")
    except:
        print('enter valid number')

def main():
    print(find_prime(),"is prime")
main()

