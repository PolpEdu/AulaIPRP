#Eduardo Nunes
from turtle import *
screen = Screen()
screen.setup(800, 800)

def espiralEstrelas(variante,vezes):
    for i in range(vezes+1):
        i=1
        left(144)
        forward(100*i)

espiralEstrelas(0,10)
done()