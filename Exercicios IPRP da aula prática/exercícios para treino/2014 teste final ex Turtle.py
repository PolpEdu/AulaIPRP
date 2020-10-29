from turtle import *
import random
import math

speed(9)
width(5)

hideturtle()

def desenhar(raio):
    up()
    goto(0, -raio)
    down()
    for x in range(4,0,-1):
        if x%2!=0:
            fillcolor("white")
        elif x %2 ==0:
            fillcolor("black")
        begin_fill()
        up()
        goto(0, -raio * x * 0.25)
        down()
        circle(raio * x * 0.25)
        end_fill()

    def shot(raio):
        x = random.randint(-raio, raio)
        y = random.randint(-raio, raio)
        d = math.sqrt(abs(0 - x) ** 2 + abs(0 - y) ** 2)
        if d >= raio:
            return

        up()
        goto(x, y)
        color("red", "red")
        begin_fill()
        circle(raio / 25)
        end_fill()
        down()

    while True:
        shot(raio)

desenhar(200)
