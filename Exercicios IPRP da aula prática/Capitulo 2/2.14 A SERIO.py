# Eduardo Nunes
from turtle import *

screen = Screen()
screen.setup(800, 800)
pensize(1)


def quadrado(espaço, vezes):
    speed(vezes/5) #para ser mais ou menos o mesmo tempo
    distancia = vezes*10
    penup()
    goto(-distancia/2, -distancia/2) #de modo a ficar no centro do ecrã no final da construção da figura
    pendown()

    for i in range(vezes + 1):
        retirar = i * espaço * 2 # a nova distância tem que se tirar o i duas vezes por causa do outro lado
        novadist = distancia - retirar

        # i nao pode ser = 0
        setheading(0)
        if i ==0:
            i=1

        for x in range(4):
            forward(novadist)
            left(90)

        if novadist <= 10:  # usei aqui 10 para nao ficar simplesmente com quadrados super pequenos
            hideturtle()
            Terminator()
            done()
            return  # se for negativo parar porque se nao continua a fazer para o sentido oposto (distancia negativa)

        print(novadist)
        # defino a nova posição do novo quadrado

        penup()
        forward(espaço)
        left(90)
        forward(espaço)
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


try:
    espaco = int(input("Espaço. Nota: a figura poderá deixar de ter os quadrados desejados se mudar o espaço minimo entre eles(5 minimo e máximo 10): "))
    if espaco < 5 or espaco > 10:
        espaco = 5
except:
    print("O espaço tem que ser um numero inteiro")
    espaco = 5

showturtle()
clear()

print("Com", vezes, "vezes e com um espaço de", espaco, "a figura será:")
quadrado(espaco, vezes)

