# Eduardo Nunes
from turtle import *

screen = Screen()
screen.setup(900, 850)
pensize(1)
speed(5)
penup()

def desenhar(raio):
    goto(-raio*2,0)
    pendown()
    right(90)
    circle(raio,180)
    circle(-raio,180)

desenhar(100)
hideturtle()
Terminator()
done()