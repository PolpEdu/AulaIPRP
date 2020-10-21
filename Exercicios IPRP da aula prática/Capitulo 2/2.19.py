# Eduardo Nunes
from turtle import *

screen = Screen()
screen.setup(900, 850)
pensize(3)
color("black", "white")
speed(10)
penup()
hideturtle()


def desenho(raio):
    goto(-raio, raio)
    down()
    inverted = 1
    for x in range(3):
        setheading(0)
        for i in range(3):
            begin_fill()
            circle(abs(raio) * 0.25)
            end_fill()
            if i == 2:
                setheading(-90)
                up()
                forward(raio)
                down()
                break
            up()
            forward(raio * inverted)
            down()
        inverted = inverted * -1

    #fazer com que detete os clicks
    onclick()

desenho(100)
Terminator()
done()
