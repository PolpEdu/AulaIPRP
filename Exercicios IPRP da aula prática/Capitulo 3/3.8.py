# Eduardo Nunes
import math

def f(x):
    y = math.pow(x, 3) - x - 1
    return y


def zeroounao(x1):
    # Corolário do Teorema Bolzano-Cauchy (ou Teorema do Valor médio)
    #para comecarem a mesma distancia
    erro = 0.1
    x2 = -x1
    virei = 0
    while abs(f(x1)) > 10 ** -10:
        y1 = f(x1)
        y2 = f(x2)
        troca = 0
        #print(f"{x1},{x2}")
        if virei == 0:
            if y1 * y2 < 0:
                x2 += erro
            else:
                x2 -=erro
                virei = 1
        else:
            if y1 * y2 < 0:
                x1 -= erro
            else:
                x2 += erro
                print(f"Zero está entre {x1},{x2}")
                break

zeroounao(40)