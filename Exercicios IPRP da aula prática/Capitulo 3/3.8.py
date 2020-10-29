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
    print(x2)
    while abs(f(x1)) > 10 ** -10:
        y1 = f(x1)
        y2 = f(x2)
        troca = 0
        print(f"{x1},{x2}")
        if y1 * y2 < 0:
            if troca == 0:
                print("Contido, vou agora aumentar x2")
                x2 += erro

            elif troca == 1:
                print("Contido, vou diminuir x1")
                x1-=erro

        else:
            if troca == 0:
                troca =1
                print("Nao contido, vou aumentar x1")
                x2 -= erro #vou tirar para refazer a ultima conta
            else:
                x1 +=erro
                print(f"{x1},{x2}")
zeroounao(10)