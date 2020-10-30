# Eduardo Nunes
from turtle import *

width(2)
speed(1)


def andar(string, d,angulo):
    for x in string:
        if x == 'f':
            forward(d)
        elif x == 'd':
            right(angulo)
        elif x == 'e':
            left(angulo)
        elif x == 't':
            forward(-d)


andar("feftd", 100,90)
done()
Terminator()
