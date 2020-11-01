from turtle import *
import math


def desenhar(x, y, comprimento, largura, espacoentre):
    up()
    goto(x, y)
    setheading(0)
    down()
    for x in range(2):
        vezesC = comprimento / espacoentre

        if comprimento % vezesC == 0:
            restoC = 0
        else:
            restoC = espacoentre * (vezesC - math.floor(vezesC))

        print(restoC)
        for x in range(math.floor(vezesC) + 1):
            down()
            forward(espacoentre)
            up()
            forward(espacoentre)

        down()
        forward(espacoentre)
        up()
        forward(espacoentre - restoC)
        right(90)

        vezesL = largura / espacoentre

        if comprimento % vezesC == 0:
            restoL = 0
        else:
            restoL = espacoentre * (vezesL - math.floor(vezesL))

        for x in range(math.floor(vezesL) + 1):
            down()
            forward(espacoentre)
            up()
            forward(espacoentre)

        down()
        forward(espacoentre)
        up()
        forward(espacoentre - restoL)
        right(90)


desenhar(-100 / 2, 150 / 2, 100, 150, 11)
done()
Terminator()
