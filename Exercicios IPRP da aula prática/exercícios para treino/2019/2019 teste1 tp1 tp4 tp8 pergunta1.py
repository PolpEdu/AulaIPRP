# pergunta 1

# 1o erro:
# razies não esta defenida no escopo da função, assim vai dar um erro.
# uma solução seria defenir as duas razies numa lista chamada "raizes" e,
# depois dar print a essa lista, como por exemplo:

# razieslista =[raiz1,raiz2]

# if raiz1 == raiz2 :
#	print ( " Solucao : " , raiz1 )
# else :
#	print ( " Solucoes : " , raizeslista )

# 2o erro:
# Não foi chamado o modulo math para calcular a raiz quadrada do discriminante.

# um codigo corrigido poderia ser:
import math


def raizes(a, b, c):
    discriminante = b ** 2 - 4 * a * c
    if a == 0 or discriminante < 0:
        print(" Erro ")
    else:
        raiz_disc = math.sqrt(discriminante)
        raiz1 = float((- b + raiz_disc)) / (2 * a)
        raiz2 = float((- b - raiz_disc)) / (2 * a)

        raizes = [raiz1, raiz2]
        if raiz1 == raiz2:
            print(" Solucao : ", raiz1)
        else:
            print(" Solucoes : ", raizes)


raizes(1, 2, -5)
