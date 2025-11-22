import math


def math_func_NOT(x):
    y = (x**3) - (2 * x) - 5
    return y

def math_func(x):
    x_1 = 3 * x
    y = math.e**x_1 + x_1 - 5
    return y

def math_func_der_NOT(x):
    y = (3 * (x**2)) - 2
    return y
    
def math_func_der(x):
    x_1 = 3 * x
    y = (3 * (math.e**x_1)) + 3
    return y    
    
def newt(x_0):
    x_1 = x_0 - (math_func(x_0) / math_func_der(x_0))
    #print(math_func(x_0), math_func_der(x_0))
    return x_1

x_0 = 1
x_1 = 0


run = True
iter = 0
while run == True and iter <= 20:
    print(x_0, x_1)
    if round(x_0, 5) == round(x_1, 5):
        run == False
        print("Nollvärde = " + str(round(x_0, 5)))
    else:
        x_1 = newt(x_0)
        x_0 = x_1
    
        print(x_0)

    iter += 1
    print(iter)
    