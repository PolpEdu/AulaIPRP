from turtle import *
import math

width(2)


# feito quase tudo no notepad
def desenhar(comprimentobase, lados, nrtravessas):
    espacoporlado = lados / nrtravessas
    angulodocant = math.degrees(math.acos((comprimentobase / 2) / lados))
    angulotopo = 180 - 2 * angulodocant

    # desenhar o Triangulo
    forward(comprimentobase)
    left(180 - angulodocant)
    forward(lados)
    left(180 - angulotopo)
    forward(lados)
    setheading(0)

    ###############################################

    medidatirada = math.cos(math.radians(angulodocant)) * espacoporlado
    for x in range(nrtravessas):
        tirado = 2* x * medidatirada
        print(tirado)

        forward(comprimentobase - tirado)
        if x == 0 or x % 2 == 0:
            left(180 - angulodocant)
        elif x == 1 or x % 2 != 0:
            right(180- angulodocant)

        forward(espacoporlado)
        if x == 0 or x % 2 == 0:
            left(angulodocant)
        elif x == 1 or x % 2 != 0:
            right(angulodocant)


desenhar(200, 250, 10)
hideturtle()
done()
Terminator()
