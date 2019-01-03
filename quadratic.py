#write a Python program to solve quadratic equation
def quadr():
    a = int(input('enter a value:'))
    b = int(input('enter b value:'))
    c = int(input('enter c value:'))
    
    #quadratic equation is b^2-4ac
    d = (b ** 2) - (4 * a * c)
    return d
quadr()

