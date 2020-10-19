# Eduardo Nunes
from turtle import *

screen = Screen()
screen.setup(900, 850)
pensize(1)
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
    for x in range(3):
        penup()
        goto(0,0)
        pendown()
        begin_fill()
        if x ==0:
            forward(rcirculo)
        elif x ==1:
            forward(-rcirculo)
        elif x ==2:
            left(45)
            forward(rcirculo)
        left(90)
        circle(rcirculo,45)
        left(90)
        forward(rcirculo)
        end_fill()

    #circulo centro
    color("yellow", "black")
    goto(0,-raio*0.25)
    circle(raio*0.25)

desenhar(150)
hideturtle()
Terminator()
done()