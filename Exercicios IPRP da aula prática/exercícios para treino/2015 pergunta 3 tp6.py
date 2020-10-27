from turtle import *
import random

speed(5)
width(2)


def desenhar(livros, larguralivro, alturamax, alturalivromin):
    up()
    goto((-livros * larguralivro) / 2, 0)
    down()
    for x in range(2):
        forward(livros * larguralivro)
        left(90)
        forward(alturamax)
        left(90)

    for x in range(livros):
        altura = random.randint(alturalivromin, alturamax)
        for i in range(2):
            forward(larguralivro)
            left(90)
            forward(altura)
            left(90)
        forward(larguralivro)


desenhar(10, 30, 100, 60)

done()
Terminator()
hideturtle()
