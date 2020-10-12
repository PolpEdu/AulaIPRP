# Eduardo Nunes
from turtle import *

screen = Screen()
screen.setup(800, 800)


def espiralEstrelas(variante, vezes):
    for i in range(vezes + 1):
        #i nao pode ser = 0
        i += 1
        right(144)
        forward(10 * i * variante)


clear()
hideturtle()
write("Selecionar Valores na consola...", font=40, align="center")

try:
    vezes = int(input("Quantas linhas queres para desenhar na estrela? "))
except:
    print("O número de vezes tem de ser um numero inteiro (100 default).")
    vezes = 100

try:
    variante = int(input("Multiplicador (1 default): "))
except:
    variante = 1

showturtle()
clear()
print("Com", vezes, "vezes e com um multiplicador de", variante, "a figura será:")
espiralEstrelas(variante, vezes)

Terminator()
done()
