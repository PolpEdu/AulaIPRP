#Eduardo Nunes
import math

def Polinomio(x):
    y = math.pow(x,4) + math.pow(x,3) + 2*math.pow(x,2) - x
    return y

x1 = Polinomio(1.1)
print(x1)
x2 = Polinomio(5)
print(x2)
x3 = Polinomio(2/3)
print(x3)