#Eduardo Nunes
import math

def desordem(numeroobjetos1, numeroobjetos2):
    proporcao =0
    numeroobejtostotais = numeroobjetos1 + numeroobjetos2


    for x in range(0,2):
        #print(x)
        if x  == 0:
            divisao = numeroobjetos1/numeroobejtostotais
            #print(divisao)
        else:
            divisao = numeroobjetos2/numeroobejtostotais
            #print(divisao)

        proporcao = divisao* math.log(2,divisao) + proporcao
        print(proporcao)

    proporcao = -1*proporcao
    return proporcao

x = int(input("Numero de objetos1: "))
y = int(input("Numero de objetos2: "))

print(desordem(x,y))