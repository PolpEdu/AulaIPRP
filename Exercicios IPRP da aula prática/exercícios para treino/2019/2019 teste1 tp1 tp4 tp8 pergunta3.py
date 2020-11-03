from turtle import *
speed(26)
fillcolor("black")

def desenhar(nbrancas,cbrancas,largura):
    for x in range(1,nbrancas+1):
        for i in range(2):
            forward(largura)
            left(90)
            forward(cbrancas)
            left(90)
        forward(largura)
        if x % 4 !=0:
            teclaspreta(cbrancas,largura)
        elif x== nbrancas+1:
            forward(largura)
            right(90)
            forward(cbrancas)
            left(90)
            forward(largura)

def teclaspreta(cbrancas,largura):
    left(90)
    forward(cbrancas*0.65)

    right(90)
    begin_fill()
    for x in range(1,3):
        forward(largura*x*1/3)
        left(90)
        forward(cbrancas*0.35)
        left(90)

    forward(largura*1/3)
    end_fill()

    right(90)
    forward(cbrancas*0.65)
    left(90)


desenhar(24,200,20)
done()
Terminator()