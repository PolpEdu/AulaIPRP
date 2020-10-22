# Eduardo Nunes
from turtle import *

screen = Screen()
screen.setup(900, 850)
pensize(3)
color("black", "white")

speed(25)
penup()
hideturtle()

colors = ["green", "red"]
circlesx = []
circlesy = []
circulosSELE = [0, 0, 0, 0, 0, 0, 0, 0, 0]

player = 1
clicks =0

raio = 200

def click(x, y):
    global clicks, raio
    for i in range(9):
        d = (raio * 0.25) ** 2 - ((circlesx[i] - x) ** 2 + (circlesy[i] - y) ** 2)

        if (d >= 0):
            #so quero contar os clicks dentro do circulo
            clicks += 1

            if (clicks % 2) == 0:
                player = 2

            elif clicks % 2 != 0:
                player = 1

            if player == 1:
                print("Player 1 circulo: ", i)
                if circulosSELE[i] != 0:
                    print("Já selecionado.")
                    return
                up()
                goto(circlesx[i],circlesy[i])
                down()
                drawcross()
                up()

                circulosSELE[i] = 1

            else:
                print("Player 2 circulo: ", i)
                if circulosSELE[i] != 0:
                    print("Já selecionado.")
                    return
                up()
                goto(circlesx[i], circlesy[i])
                down()
                drawcircle(raio)
                up()
                circulosSELE[i] = 2

            if ganhei(1)==True:
                clear()
                goto(0,0)
                color("Green")
                write("O player 1 ganhou.",font=("Arial", 20, 'bold', 'italic', 'underline'))
            elif ganhei(2)==True:
                clear()
                goto(0,0)
                color("Red")
                write("O player 2 ganhou.",font=("Arial", 20, 'bold', 'italic', 'underline'))
            elif clicks ==9:
                clear()
                goto(0,0)
                color("Blue")
                write("EMPATE",font=("Arial", 20, 'bold', 'italic', 'underline'))
        else:
            # print("fora")
            continue
    #print(x, y)

def ganhei(marca):
    if circulosSELE[0] == circulosSELE[1] == circulosSELE[2] == marca:
        return True
    elif circulosSELE[5] == circulosSELE[4] == circulosSELE[3] == marca:
        return True
    elif circulosSELE[6] == circulosSELE[7] == circulosSELE[8] == marca:
        return True

    elif circulosSELE[0] == circulosSELE[5] == circulosSELE[6] == marca:
        return True
    elif circulosSELE[1] == circulosSELE[4] == circulosSELE[7] == marca:
        return True
    elif circulosSELE[2] == circulosSELE[3] == circulosSELE[8] == marca:
        return True

    elif circulosSELE[0] == circulosSELE[4] == circulosSELE[8] == marca:
        return True
    elif circulosSELE[2] == circulosSELE[4] == circulosSELE[6] == marca:
        return True
    return False

def desenho(raio):
    goto(-raio, raio)
    down()
    inverted = 1

    for x in range(3):
        setheading(0)
        for i in range(3):
            centrox = round(xcor())
            centroy = round((ycor() + raio * 0.25))
            print(centrox, centroy)

            circlesx.append(centrox)
            circlesy.append(centroy)

            circle(abs(raio) * 0.25)
            if i == 2:
                setheading(-90)
                up()
                forward(raio)
                down()
                break
            up()
            forward(raio * inverted)
            down()
        inverted = inverted * -1

def drawcross():
    color("Green")
    setheading(0)
    right(45)
    forward(35)
    backward(70)
    forward(35)
    left(90)
    forward(35)
    backward(70)

def drawcircle(raio):
    color("Red")
    setheading(90)
    up()
    forward(-raio*0.1)
    down()
    setheading(0)
    circle(raio*0.1)

onscreenclick(click)

desenho(raio)
Terminator()
done()
