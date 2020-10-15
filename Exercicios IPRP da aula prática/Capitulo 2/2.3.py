# Eduardo Nunes
from turtle import *
import random

screen = Screen()
width = 800
height = 700
screen.setup(width, height)
vezes = random.randint(1, 500)
pensize(2)

#speed(50) é engraçado

for x in range(vezes):
    x,y = position()

    #para evitar sair do ecrã
    widthScreen = width/2
    heightScreen = height/2

    if not(-widthScreen < x < widthScreen and -heightScreen < y < heightScreen):
        print(f"x:{x}, y:{y}")
        print("Sai do Ecrã!")
        penup()
        goto(0,0)
        pendown()

    graus = random.randint(0, 359) #nao pode ser 360 se nao seria = a 0

    # Vou generar 3 numeros de 0 a 1 random para fazer uma cor RGB
    # A documentação do turtle usa numeros de 0.01 a 1
    Rcor = random.uniform(0.01, 1)
    Gcor = random.uniform(0.01, 1)
    Bcor = random.uniform(0.01, 1)

    DirouEsq = random.randint(0, 1)
    distancia = random.randint(50, 200) #200 so for maior... porque se nao sai do ecrã muito facilmente
                                        #distancia minima de 50 para evitar anda 1 coordenada só

    pencolor(round(Rcor,2), round(Gcor,2), round(Bcor, 2))

    if DirouEsq == 0:
        Dir = "Direita"
        right(graus)
    else:
        Dir = "Esquerda"
        left(graus)
    forward(distancia)

    print(f"Graus: {graus}; Distancia: {distancia}; Direção: {Dir}; Com a cor: {pencolor()}; A fazer Vezes: {vezes}")

Terminator()
done()
