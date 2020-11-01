import math
from turtle import *

width(2)
speed(20)


def desenhar(x, y, raio, orientacao):
    up()
    goto(x, y)
    down()
    left(orientacao)

    divisions = math.floor(raio / 10)
    for x in range(1,divisions+1):
        hexagono(divisions*x)


def hexagono(raio):
    for x in range(6):
        for i in range(3):
            forward(raio)
            left(120)
        left(60)


desenhar(0, 0, 95, 0)
up()
goto(95,0)
down()

done()
Terminator()
