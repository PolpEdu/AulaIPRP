# Eduardo Nunes
from turtle import *

screen = Screen()
screen.setup(900, 850)
pensize(3)
color("black", "yellow")
speed(5)
penup()


# INACABADO

def desenhar(raio):
    # main quadrado
    goto(-raio, -raio)
    pendown()
    begin_fill()
    for x in range(4):
        forward(raio * 2)
        left(90)
    end_fill()
    penup()

    # circulos
    rcirculo = (-raio * 0.75)
    color("black", "black")
    goto(0, 0)
    for x in range(3):
        pendown()
        begin_fill()
        if x == 0:
            forward(rcirculo)
            left(90)
            circle(rcirculo, 60)
            left(90)
            forward(rcirculo)

        elif x == 1:
            left(60)
            forward(rcirculo)
            right(90)
            circle(-rcirculo, 60)
            right(90)
            forward(rcirculo)

        elif x == 2:
            left(60)
            forward(rcirculo)
            left(90)
            circle(rcirculo, 60)

        end_fill()
        penup()

    # circulo centro
    color("yellow", "black")
    goto(0, -raio*0.15)
    setheading(0)

    begin_fill()
    pendown()
    circle(raio * 0.15)
    end_fill()
    penup()


desenhar(150)
hideturtle()
Terminator()
done()
