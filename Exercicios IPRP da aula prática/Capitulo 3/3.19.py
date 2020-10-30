# Eduardo Nunes
from turtle import *
import random

width(2)
speed(1)
adn = 'fted'
adnlist = list(adn)


def andar(comprimento):
    adnGEN = ""
    for i in range(comprimento):
        numero = random.randint(0, 3)
        adnGEN += adnlist[numero]
        print(adnGEN)
    for x in adnGEN:
        d = random.randint(10, 200)
        angle = random.randint(1, 359)
        if x == 'f':
            forward(d)
        elif x == 'd':
            right(angle)
        elif x == 'e':
            left(angle)
        elif x == 't':
            forward(-d)

andar(10)
done()
Terminator()
