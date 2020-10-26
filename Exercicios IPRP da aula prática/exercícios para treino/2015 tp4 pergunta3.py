from turtle import *
up()
pensize(3)
speed(10)
hideturtle()

def desenhar(cor,fillcor,raio,x,y):
    color(cor,fillcor)
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



desenhar("Red","yellow",200,0,0)
hideturtle()
done()
Terminator()