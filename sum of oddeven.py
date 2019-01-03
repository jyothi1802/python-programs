#write a python program for a list that has numbers, find sum of odd numbers and sum of even numbers

def append():
    a = []
    n = int(input("Enter number of elements:"))
    for i in range(1, n + 1):
        b = int(input("Enter element:"))
        a.append(b)
    Odd_Even(a)
even = []
odd = []
def Odd_Even(x):
    for j in x:
        if j%2==0:
            even.append(j)
        else:
            odd.append(j)
append()
print("The sum of  even list", sum(even))
print("The sum of odd list", sum(odd))

