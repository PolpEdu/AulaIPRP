from turtle import *

width(1)
speed(5)
fillcolor("black")
shape("circle")

def retangulo(c, l):
    up()
    goto(-c/2, 0)
    down()

    for x in range(2):
        forward(c)
        left(90)
        forward(l)
        left(90)

    width(4)

    up()
    goto(0, 0)
    down()

    seth(90)
    up()
    forward(0.1 * l)
    down()
    forward(0.8 * l)
    up()
    forward(0.1 * l)

    width(1)
    down()


def desenhar(x1, x2, c, l):
    retangulo(c, l)
    if not 0<= x1<7 or not 0<= x2<7 :
        return print("Invalid x")
    desenharcirculos(x1, -c, l)
    desenharcirculos(x2, c, l)



def desenharcirculos(x, c, l):
    shapesize(l/120)
    if x== 0:
        return
    elif x == 1:
        drawonecenter(c,l)
    elif x == 2:
        drawtwo(c, l)
    elif x == 3:
        drawtwo(c,l)
        drawonecenter(c,l)
    elif x == 4:
        drawfour(c,l)
    elif x ==5:
        drawfour(c,l)
        drawonecenter(c,l)
    elif x == 6:
        drawsix(c,l)

def drawonecenter(c,l):
    up()
    goto(c / 4, l / 2)
    down()
    stamp()

def drawtwo(c,l):
    up()
    goto(c / 4 + c / 6, l / 2 + l / 3)
    down()
    stamp()
    up()
    goto(c / 4 - c / 6, l / 2 - l / 3)
    down()
    stamp()


def drawfour(c,l):
    up()
    goto(c / 4 + c / 6, l / 2 + l / 3)
    down()
    stamp()
    up()
    goto(c / 4 - c / 6, l / 2 + l / 3)
    down()
    stamp()
    up()
    goto(c / 4 - c / 6, l / 2 - l / 3)
    down()
    stamp()
    up()
    goto(c / 4 + c / 6, l / 2 - l / 3)
    down()
    stamp()

def drawsix(c,l):
    drawfour(c, l)
    up()
    goto(c / 4, l / 2 + l / 3)
    down()
    stamp()
    up()
    goto(c / 4, l / 2 - l / 3)
    down()
    stamp()

desenhar(6, 5, 400, 200)

done()
Terminator()
