import random
from turtle import *
#fiz em cerca de 16 minutos
#desperdicei bue tempo a pesquisar como e que se genera um double/int

#Double -- random.uniform(0,1)
#INT -- random.randint(1,10)


up()
pensize(3)
speed(20)
hideturtle()
def desenhar(raio,x,y):
    goto(x,y-raio)


    down()
    begin_fill()
    showturtle()
    circle(raio)
    end_fill()
    up()
    hideturtle()

    goto(x,y)
    left(45)
    forward(raio)
    right(90)
    down()
    begin_fill()
    showturtle()
    circle(raio*0.4)
    hideturtle()
    end_fill()
    setheading(0)
    up()

    hideturtle()
    goto(x,y)

    left(135)
    forward(raio)
    right(90)
    down()
    begin_fill()
    showturtle()
    circle(raio * 0.4)
    end_fill()
    setheading(0)
    up()


vezes = random.randint(200, 700)
for x in range(vezes):
    R = random.uniform(0, 1)
    g = random.uniform(0, 1)
    b = random.uniform(0, 1)

    xpos = random.randint(-300, 300)
    ypos = random.randint(-300, 300)
    tamanho = random.randint(1, 50)

    pencolor(R, g, b)
    fillcolor(R,g,b)
    desenhar(tamanho,xpos,ypos)

hideturtle()
done()
Terminator()