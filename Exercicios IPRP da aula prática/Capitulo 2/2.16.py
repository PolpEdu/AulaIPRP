# Eduardo Nunes
from turtle import *

screen = Screen()
screen.setup(900, 850)
speed(5)
pensize(5)
penup()

def desenhar(raio):
    colors = ["#0085C7", "#000000", "#DF0024",
              "#F4C300", "#009F3D"]
    goto(-raio-raio*1.20,0)
    for x in range(5):
        pendown()
        showturtle()
        color(colors[x])
        circle(raio)
        penup()
        hideturtle()
        forward(raio*2.20)
        if x==2:
            goto(-raio * 1.10, -raio)
            pendown()
            showturtle()


desenhar(50)
hideturtle()
Terminator()
done()