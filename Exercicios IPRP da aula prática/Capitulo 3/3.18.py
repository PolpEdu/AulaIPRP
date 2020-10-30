# Eduardo Nunes
from turtle import *
import random
width(2)
speed(1)

def andar(string):
    for x in string:
        d = random.randint(10,200)
        angle = random.randint(1,359)
        if x == 'f':
            forward(d)
        elif x == 'd':
            right(angle)
        elif x == 'e':
            left(angle)
        elif x == 't':
            forward(-d)

andar("feftd")
done()
Terminator()
