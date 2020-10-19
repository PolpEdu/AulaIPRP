# Eduardo Nunes
from turtle import *

screen = Screen()
screen.setup(900, 850)
pensize(2)
color("black", "yellow")
speed(5)
penup()

#INACABADO

def desenhar(raio):
    #main quadrado
    goto(-raio, -raio)
    pendown()
    begin_fill()
    for x in range(4):
        forward(raio*2)
        left(90)
    end_fill()
    penup()

    #circulos
    rcirculo= (-raio * 0.75)
    color("black", "black")
    goto(0, 0)
    for x in range(3):
        penup()
        pendown()
        begin_fill()
        if x ==0:
            forward(rcirculo)
            left(90)
            circle(rcirculo, 45)
            left(90)
            forward(rcirculo)
            end_fill()
        elif x ==1:
            left(45)
            forward(rcirculo)
            right(90)
            circle(-rcirculo, 45)
            right(90)
            forward(rcirculo)
        elif x ==2:
            left(90)
            forward(rcirculo)
            left(90)
            circle(rcirculo, 45)
            left(90)
            forward(rcirculo)

    #circulo centro
    color("yellow", "black")
    goto(0,-raio*0.25)
    circle(raio*0.25)

desenhar(150)
hideturtle()
Terminator()
done()