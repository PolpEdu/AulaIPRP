#Eduardo Nunes
import random
def areas(vezes):
    areatotal = 2**2
    conta = 0
    for x in range(vezes):
        atirarx =  random.uniform(0,2)
        atirary = random.uniform(0,2)
        if atirarx <1:
            if atirary<1:
                saiu = 2
            else:
                saiu = 3
        else:
            if atirary <1:
                saiu = 1
            else:
                if atirary >atirarx:
                    saiu = 4
                else:
                    saiu = 3
        if saiu % 2 != 0:
            conta+=1
    percentagem = (conta / vezes)*100

    #interessante:
    regiaoimpar = areatotal* percentagem/100
    regiaopar = areatotal-regiaoimpar



    print(f"Percentagem resposta: {percentagem}%\n"
          f"Area regiao par aproximado: {regiaopar}\n"
          f"Area regiao impar aproximado: {regiaoimpar}\n")
areas(100000)