from turtle import *
import random

up()
goto(0, 0)
down()
width(2)
speed(50)

def desenharGrafico(maxX, maxY, linhas, pontos):
    forward(maxX)
    stamp()
    up()
    goto(0, 0)
    seth(90)
    down()
    forward(maxY)
    stamp()
    up()

    for j in range(linhas):
        xarr = []
        yarr = []
        # dou reset para cada linha a array
        r = random.uniform(0, 1)
        g = random.uniform(0, 1)
        b = random.uniform(0, 1)

        print(f"{r}, {g}, {b}")
        pencolor(r, g, b)

        up()
        goto(0, 0)
        down()
        for x in range(pontos):
            while True:
                if x == 0:
                    xold = 0
                    yold = 0
                else:
                    xold = xarr[x - 1]
                    yold = yarr[x - 1]
                xnew = random.randint(xold, maxX)
                ynew = random.randint(yold, maxY)
                # print(f"{xnew},{ynew}")
                if xnew >= xold and ynew >= yold:
                    xarr.append(xnew)
                    yarr.append(ynew)
                    #print(f"{xarr}\n{yarr}")
                    goto(xnew, ynew)
                    break


desenharGrafico(350, 350, 25, 5)

done()
Terminator()
