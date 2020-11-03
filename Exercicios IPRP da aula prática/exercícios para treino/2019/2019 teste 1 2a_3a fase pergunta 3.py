from turtle import *
import math

speed(5)
colors = ["yellow", "blue"]
up()


def triangulos(n, espacoportriangulo):

    distancia = espacoportriangulo * n
    tamanho = math.sin(math.pi/3)*(distancia*2+espacoportriangulo*2)
    print(tamanho)
    goto(0, -distancia)
    for x in range(n):
        fillcolor(colors[x % 2])
        pencolor(colors[x % 2])
        seth(-60)

        down()

        begin_fill()
        for i in range(3):
            left(120)
            forward(tamanho-espacoportriangulo*x*2)
        end_fill()

        up()
        seth(90)
        forward(espacoportriangulo)


triangulos(6, 23)
done()
Terminator()
