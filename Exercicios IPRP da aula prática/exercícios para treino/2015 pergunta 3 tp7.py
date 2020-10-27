from turtle import *
width(2)
speed(15)

#100
#9 ondas
def desenhar(ondas,altura,largura):
    up()
    goto((-(largura*ondas)+(largura/2))/2,0)
    down()
    raio = largura/ondas
    setheading(-90)
    for x in range(ondas):
        circle(raio,180)
        circle(-raio, 180)

    circle(raio,180)
    forward(altura)
    left(90)
    forward((largura*ondas)+(largura/2))
    left(90)
    forward(altura)


desenhar(4,200,100)
hideturtle()
done()
Terminator()
