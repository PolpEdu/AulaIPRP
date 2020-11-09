# Eduardo Nunes
import os
import time
clear =lambda : os.system('cls')

while True:
    try:
        fn = int(input("Frequência de nascimentos (minutos): "))
        fl = int(input("Frequência de falecimentos (minutos): "))
        fe = int(input("Frequência de emigração (minutos): "))
        pi = int(input("População Inicial: "))
        anos = int(input("Por quantos anos: "))
    except:
        fn = 20
        fl = 15
        fe = 10
        pi = 10000000
        anos = 1
    print("Resumo dos dados:\n"
          "-----------------\n"
          "Frequência de nascimentos  (minutos): %2d\n"
          "Frequência de mortes  (minutos): %2d\n"
          "Frequência de emigrantes  (minutos): %2d\n"
          "População Inicial: %9d" % (fn, fl, fe, pi))


    def estimar(fn, fl, fe, pi):
        #de 20 em 20 minutos nasce uma pessoa!!!
        #nao é: nascerem 20 em 1 minuto
        freqnasc = (60/fn) * 24 * 365
        freqmort = (60/fl)  * 24 * 365
        freqemigrante = (60/fe) * 24 * 365
        estima = (pi+ freqnasc) - (freqmort + freqemigrante)

        return estima

    for x in range(anos):
        estimado = estimar(fn, fl, fe, pi)
        if estimado <= 0:
            print("O pais vai ficar deserto.")
            break
        pi = estimado


    print("-----------------\n"
          "Estimativa: \n"
          "A população terá ao final de %1d ano(s): %7d\n" % (anos,estimado))

    time.sleep(20)
    clear()