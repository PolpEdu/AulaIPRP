#mano questa merda....
from turtle import *
width(2)

def desenhar(lado, comprimentoboca, cn, cy, co):
    up()
    goto(-lado / 2, 0)
    down()
    for x in range(4):
        forward(lado)
        left(90)

    for a in range(2):
        up()
        if a == 0:
            goto(-lado / 2, lado - (cy * 5))
            color("black", "green")
            down()
            begin_fill()
            for i in range(2):

                forward(-co / 3)
                left(90)
                forward(co)
                left(90)
        else:
            goto(lado / 2, lado - (cy * 5))
            color("black", "green")
            down()
            begin_fill()
            for i in range(2):

                forward(co / 3)
                left(90)
                forward(co)
                left(90)

        end_fill()

    up()
    goto(-comprimentoboca / 2, comprimentoboca)
    down()

    color("black", "yellow")
    begin_fill()
    for i in range(2):
        forward(comprimentoboca)
        left(90)
        forward(comprimentoboca / 3)
        left(90)
    end_fill()

    up()
    goto(-(cn / 6) / 2, comprimentoboca + comprimentoboca / 3 + cn / 1.5)
    down()

    color("black", "red")
    begin_fill()
    for i in range(2):
        forward(cn / 6)
        left(90)
        forward(cn)
        left(90)
    end_fill()

    up()
    goto(-(comprimentoboca / 2) - comprimentoboca, lado - cy*3)
    down()

    color("black", "blue")
    begin_fill()
    for i in range(4):
        forward(cy)
        left(90)
    end_fill()

    up()
    goto(comprimentoboca/2, lado - cy*3)
    down()

    color("black", "blue")
    begin_fill()
    for i in range(4):
        forward(cy)
        left(90)
    end_fill()


desenhar(200, 25, 40, 20, 45)
hideturtle()
done()
Terminator()
