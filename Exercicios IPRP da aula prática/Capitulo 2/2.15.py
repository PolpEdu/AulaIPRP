# Eduardo Nunes
from turtle import *

screen = Screen()
screen.setup(800, 800)
pensize(1)
#nao esta exatamente como quero

def desenhar(vezes):
    distanciainical = 30
    diferençagraus= 5
    setheading(260)
    for i in range(vezes):
        left(diferençagraus*i)
        for x in range(4):
            forward(distanciainical*(i+1))
            left(90)

clear()
hideturtle()
write("Selecionar Valores na consola...", font=40, align="center")

try:
    vezes = int(input("Quantos quadrados queres desenhar? (minimo 3) "))
    if vezes < 3:
        vezes = 3
except:
    print("O número de vezes tem de ser um numero inteiro.")
    vezes = 20


showturtle()
clear()

print(f"Com {vezes} vezes será...")
desenhar(vezes)


Terminator()
done()