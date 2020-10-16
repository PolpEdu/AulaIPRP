# Eduardo Nunes
from turtle import *

screen = Screen()
screen.setup(800, 800)
pensize(1)


def quadrado(vezes):
    speed(vezes/5) #para ser mais ou menos o mesmo tempo
    distancia = vezes*10
    penup()
    pos = -distancia/2
    goto(pos, pos) #de modo a ficar no centro do ecrã no final da construção da figura
    pendown()

    for i in range(vezes + 1):
        retirar = i * 10 # a nova distância tem que se tirar o i duas vezes por causa do outro lado
        novadist = distancia - retirar

        # i nao pode ser = 0
        setheading(0)

        for x in range(4):
            forward(novadist)
            left(90)

        #print(novadist)


        if novadist <= 10:  # usei aqui 10 para nao ficar simplesmente com quadrados super pequenos
            hideturtle()
            Terminator()
            done()
            return  # se for negativo parar porque se nao continua a fazer para o sentido oposto (distancia negativa)

        # defino a nova posição do novo quadrado
        penup()
        forward(5)
        left(90)
        forward(5)
        pendown()


clear()
hideturtle()
write("Selecionar Valores na consola...", font=40, align="center")

try:
    vezes = int(input("Quantos quadrados queres desenhar? (minimo 10) "))
    if vezes < 10:
        vezes = 10
except:
    print("O número de vezes tem de ser um numero inteiro.")
    vezes = 10

showturtle()
clear()

print("Com", vezes, "vezes a figura será:")
quadrado(vezes)

