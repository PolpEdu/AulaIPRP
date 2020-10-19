# Eduardo Nunes
from turtle import *

screen = Screen()
screen.setup(900, 850)
pensize(1)
speed(5)
shape('turtle')
turtlesize(0.75)
color("red")
bgcolor("blue")

def desenhar(quantidade,espaco):
    penup()
    for i in range(quantidade):
        forward(espaco)
        right(24)
        espaco+=4
        stamp()

desenhar(100,10)
hideturtle()
Terminator()
done()