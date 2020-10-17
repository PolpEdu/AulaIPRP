# Eduardo Nunes
from turtle import *

screen = Screen()
screen.setup(800, 800)
pensize(1)

def desenhar(vezes,distanciainicial,diferencagraus):
    speed(vezes/1.5)
    setheading(260)
    for i in range(1, vezes+1):
        left(diferencagraus)
        for x in range(4):
            forward(distanciainicial*(i/2.5))
            left(90)

clear()
hideturtle()
write("Selecionar Valores na consola...", font=40, align="center")

try:
    vezes = int(input("Quantos quadrados queres desenhar? (minimo 3, default 20) "))
    if vezes < 3:
        vezes = 20
except:
    print("O número de vezes tem de ser um numero inteiro.\n")
    vezes = 20

try:
    distanciainicial = int(input("Qual a distancia inicial? (minimo 5, default 25) "))
    if distanciainicial < 5:
        distanciainicial = 25
except:
    print("A distancia tem que ser um numero inteiro positivo.\n")
    distanciainicial = 25


try:
    diferencagraus = int(input("Qual a diferença de graus entre quadrados? (máximo 45, default 10) "))
    if diferencagraus > 45:
        diferencagraus = 10
except:
    print("A diferença de graus tem que ser um numero menor que 45.\n")
    diferencagraus = 10

showturtle()
clear()


print(f"Com {vezes} vezes, {distanciainicial} de distancia inicial e uma diferença de graus de {diferencagraus} graus a figura será...")
desenhar(vezes, distanciainicial, diferencagraus)
Terminator()
done()