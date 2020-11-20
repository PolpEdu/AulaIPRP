# Eduardo Nunes
from turtle import *
import random

fr = 25


def desenharcampo(size, fr):
    speed(10000)
    pencolor("grey")
    up()
    goto(-size * fr / 2, -size * fr / 2)
    down()
    for y in range(8):
        for x in range(8):
            for i in range(4):
                forward(fr)
                left(90)
            forward(fr)
        if y % 2 == 0:
            left(90)
            forward(fr * 2)
            left(90)
        else:
            right(180)
    hideturtle()


def caminho(size, fr):
    pencolor("red")
    color("red", "red")
    x_cor = 0
    y_cor = 0
    speed(3)
    up()
    goto(0, 0)
    shapesize(0.5)
    shape("circle")

    stamp()

    shape("arrow")
    down()
    showturtle()

    limitex = (size* fr)//2
    limitey = (size * fr)//2

    print(limitex,limitey)

    while True:
        direcao = random.choice([0,1,2,3])
        print(direcao)
        if direcao == 1 and limitey >y_cor: #cima
            y_cor += fr
            seth(90 * direcao)
            forward(fr)
        if direcao == 0 and limitex>x_cor: #direita
            x_cor += fr
            seth(90 * direcao)
            forward(fr)
        if direcao == 3 and y_cor>-limitey: #baixo
            y_cor -= fr
            seth(90 * direcao)
            forward(fr)
        if direcao == 2 and x_cor>-limitex: #esquerda
            x_cor -= fr
            seth(90 * direcao)
            forward(fr)
        print(x_cor, y_cor)



desenharcampo(8, 30)
caminho(8, 30)
