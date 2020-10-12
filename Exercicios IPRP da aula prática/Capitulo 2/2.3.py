# Eduardo Nunes
from turtle import *
import random

screen = Screen()
width = 800
height = 800

screen.setup(width, height)

vezes = random.randint(1, 500)

for x in range(vezes):
    graus = random.randint(0, 359) #nao pode ser 360 se nao seria = a 0

    # Vou generar 3 numeros de 0 a 255 random para fazer uma cor RGB
    Rcor = random.randint(0, 255)
    Gcor = random.randint(0, 255)
    Bcor = random.randint(0, 255)

    DirouEsq = random.randint(0, 1)
    distancia = random.randint(0, 100) #100 porque se nao sai do ecrã muito facilmente

    pencolor("red")


    x,y = position()

    #para evitar sair do ecrã
    #if -width < x < width and -height < y < height:
    #    break
    if DirouEsq == 0:
        Dir = "Direita"
        right(graus)
    else:
        Dir = "Esquerda"
        left(graus)
    forward(distancia)

    print(f"Graus: {graus}; Distancia: {distancia}; Direção: {Dir}; A fazer Vezes: {vezes}")

Terminator()
done()
