# Eduardo Nunes
from turtle import *

up()
pensize(2)
speed(6)
color("black")

def desenhar(raio):
    goto(-raio, 0)
    setheading(90)

    down()
    circle(-raio)
    setheading(90)

    fillcolor("black")
    begin_fill()
    circle(-raio / 2, 180)
    circle(raio / 2, 180)
    #para dar fill bem
    circle(raio, -180)
    end_fill()

    up()
    goto(-(raio / 2) + raio * 0.12, 0)
    down()

    fillcolor("white")
    begin_fill()
    circle(-raio * 0.12)
    end_fill()
    up()

    up()
    goto((raio / 2) - raio * 0.12, 0)
    down()

    fillcolor("black")
    begin_fill()
    circle(raio * 0.12)
    end_fill()
    up()


desenhar(100)
Terminator()
done()
