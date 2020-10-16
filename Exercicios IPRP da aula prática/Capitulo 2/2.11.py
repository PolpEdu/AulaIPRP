# Eduardo Nunes
from turtle import *

screen = Screen()
screen.setup(800, 800)
pensize(1)
speed(2)

def escrevehexagono(distancia):
     #os triangulos sao todos equilateros
    for x in range(6):
        left(60)
        for x in range(3):
            forward(distancia)
            right(120)

escrevehexagono(100)
hideturtle()

done()
