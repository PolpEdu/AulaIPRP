from turtle import *
import math

pi = math.pi
speed(10)
fillcolor("black")


def hexagono(d):
    for x in range(6):
        forward(d)
        left(60)

def figura(linhas,colunas,d):
    #baixo
    ladoh = math.sin(pi / 3) * d
    espaco = (math.cos(pi / 3) * d)*1/3
    hexspace = d * 2 + espaco/3

    xi = d*6+espaco*2
    yi = ladoh*5 + espaco*2
    up()
    goto(-xi,-yi)
    down()
    for x in range(1,colunas+1):
        down()
        for i in range(linhas):
            if i % 2 == 0 or i ==0:
                hexagono(d)
            else:
                begin_fill()
                hexagono(d)
                end_fill()
            seth(90)
            up()
            forward(ladoh*2+espaco)
            down()
            setheading(0)
        up()
        if x % 2 == 1:
            goto(-xi+hexspace*x,-yi+ladoh)
        else:
            goto(-xi+hexspace*x, -yi)


figura(5,6,50)
hideturtle()

done()
Terminator()