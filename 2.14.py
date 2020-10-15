# Eduardo Nunes
from turtle import *

screen = Screen()
screen.setup(800, 800)
pensize(1)
speed(2)

# Eduardo Nunes
from turtle import *

screen = Screen()
screen.setup(800, 800)

speed(50)
#cool stuff
goto(-400, -400)
def quadrado(variante, vezes):
    for i in range(vezes + 1):
        #i nao pode ser = 0
        setheading(0)
        i +=1
        for x in range(4):
            forward(100 * variante)
            left(90)

        penup()
        forward(5)
        left(90)
        forward(5)
        pendown()



clear()
hideturtle()
#write("Selecionar Valores na consola...", font=40, align="center")

#try:
#    vezes = int(input("Quantas linhas queres para desenhar quadrados? "))
#except:
#    print("O número de vezes tem de ser um numero inteiro (10 default).")
#    vezes = 10

#try:
#    variante = int(input("Multiplicador (1 default): "))
#except:
#    variante = 1

showturtle()
clear()

vezes = 100
variante = 1

print("Com", vezes, "vezes e com um multiplicador de", variante, "a figura será:")
quadrado(variante, vezes)

Terminator()
done()


done()
