from turtle import *
width(2)
speed(7)
setheading(90)

def desenhar(numero,cor,corfill):
    color(cor,corfill)
    for x in range(numero):
        for x in range(2):
            begin_fill()
            forward(200)
            right(90)
            forward(100)
            end_fill()
            right(90)

        angulo = 360 / numero
        right(angulo)

desenhar(16,"black","orange")
hideturtle()
done()
Terminator()