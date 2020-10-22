#Eduardo Nunes
import math

def areatriangulo(a,b,c):
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

l1 = int(input("Lado 1:"))
l2 = int(input("Lado 2:"))
l3 = int(input("Lado 3:"))

print("Area Triangulo: " + str(areatriangulo(l1,l2,l3)))