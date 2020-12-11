 # Eduardo Nunes
#eu acho que estamos nos a referir a esta correlação
#https://pt.wikipedia.org/wiki/Coeficiente_de_correla%C3%A7%C3%A3o_de_Pearson
# DESVIO: https://www.todamateria.com.br/desvio-padrao/
import math
F1 = "files/Crescimento do Produto Interno Burto, Zona Euro.txt"
F2 = "files/Desemprego na Zona Euro.txt"


def coeficienterelacaoentreData(F1, F2,linhas):
    DADOS1 = getdata(F1, linhas)
    DADOS2 = getdata(F2, linhas)

    valor = coeficienterelacaoentreData(DADOS1,DADOS2)
    return valor

def getdata(F, linha):
    # le
    with open(F, "r") as fr:
        dados = fr.readlines()[1:linha]
        fr.close()
    # retira dados
    dados_list = []
    for linha in dados:
        dados_list.append(float(linha.split(" ")[2]))
    return dados_list


def coeficienterelacaoentreData(d1,d2):
    media_a = media(d1)
    media_b = media(d2)
    desvio_A = di(d1)
    desvio_B = di(d2)
    somaNUM = 0.0
    somaDEN = 0.0
    for x in range(len(d1)):
        somaNUM = somaNUM + (d1[x]- media_a) * (d2[x]- media_b)
    somaDEN = desvio_A * desvio_B * len(d1) #???? ACABAR ISTO
    return float(somaNUM/somaDEN)

def media(lista):
    return sum(lista)/len(lista)

def di(lista):
    soma = 0.0
    for i in lista:
         soma = soma + (i-media(lista))**2
    return math.sqrt(float(soma)/len(lista)-1) #desvio