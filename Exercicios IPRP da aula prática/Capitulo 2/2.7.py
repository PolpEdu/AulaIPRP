# Eduardo Nunes
from turtle import *

screen = Screen()
screen.setup(800, 800)
pensize(1)
speed(10)
penup()

def sorriso(raio):
    goto(0,-raio)
    pendown()
    circle(raio)
    for x in range(2):
        if x == 0:
            penup()
            goto(-raio * 0.35, raio * 0.25)
            pendown()

        else:
            penup()
            goto(raio * 0.35, raio * 0.25)
            pendown()

        begin_fill()
        circle(raio * 0.15)
        end_fill()

    penup()
    goto(-raio*0.4, -raio*0.5)
    pendown()

    right(20)
    circle(raio*1.2, 45)



sorriso(200)
hideturtle()
Terminator()
done()