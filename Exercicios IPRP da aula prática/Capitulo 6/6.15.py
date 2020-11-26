#Eduardo Nunes
from random import randint


dicionario = {
    "Bernardo Silva":[123456789,1.90,74],
    "Fernando Pessoa":[133712320,1.60,65],
    "Verónica Matos":[190332964,1.50,50],
    "Manuel Luis Gocha":[154321982,1.80,65],
    "Cristina Ferreira":[119665433,1.7,65],
    "Fernando Mendes":[154322199,1.79,89],
    "João Baião":[129034827,1.80,75]
}

def pessoa(dicionario):
    for k,v in dicionario.items():
        print(dicionario[k][2],(dicionario[k][1])**2)
        massacorp= dicionario[k][2]/(dicionario[k][1])**2
        dicionario[k].append(round(massacorp,2))
    return dicionario
print(pessoa(dicionario))
#https://codeshare.io/aJEPDR
