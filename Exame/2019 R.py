from turtle import *
import math

pencolor("black")


def line(comp, espaca):
    timesfor = math.floor(comp / (espaca * 2))
    restoforward = comp % (espaca * 2)

    for x in range(timesfor):
        forward(espaca)
        if pencolor() == "black":
            pencolor("white")
        else:
            pencolor("black")
        forward(espaca)

    pencolor("black")
    if restoforward - espaca < espaca:
        restocor = restoforward - espaca
        forward(espaca)
        if pencolor() == "black":
            pencolor("white")
        else:
            pencolor("black")
        forward(restocor)
    else:
        forward(restoforward)


def desenhar(x, y, comp, larg, espaca):
    up()
    goto(x, y)
    down()
    seth(0)

    for x in range(2):
        line(comp, espaca)
        right(90)
        line(larg, espaca)
        right(90)


# desenhar(0, 0,200, 80, 9)
# Terminator()
# 2)
def melhor_carga(lista, quanti):
    listposs = []
    listpesname = []
    listpes = []

    for legum1 in lista:
        for legum2 in lista:
            if legum1[1] + legum2[1] <= quanti:
                listposs.append([[legum1[0], legum1[2]], [legum2[0], legum2[2]]])

    for pairs in listposs:
        pessum = int(pairs[0][1]) + int(pairs[1][1])
        listpesname.append([str(pairs[0][0]) + "," + str(pairs[1][0]), pessum])
        listpes.append(pessum)

    maxvalue = max(listpes)

    for pares in listpesname:
        if maxvalue == pares[1]:
            split = pares[0].split(",")
            a = (split[0], split[1])
            return a


lista_carga = [('arroz', 40, 100), ('alface', 60, 200), ('batata', 80, 200), ('cenoura', 120, 250)]
#print(melhor_carga(lista_carga, 100))


def melhor_carga(lista, quanti):
    listposs = []
    listpesname = []
    listpes = []

    for legum1 in lista:
        for legum2 in lista:
            if legum1[1] + legum2[1] <= quanti:
                listposs.append([[legum1[0], legum1[2]], [legum2[0], legum2[2]]])

    for pairs in listposs:
        pessum = int(pairs[0][1]) + int(pairs[1][1])
        listpesname.append([str(pairs[0][0]) + "," + str(pairs[1][0]), pessum])
        listpes.append(pessum)

    maxvalue = max(listpes)

    for pares in listpesname:
        if maxvalue == pares[1]:
            split = pares[0].split(",")
            a = (split[0], split[1])
            return a


# 5)
Path = "Ficheiro.txt"


def ler(PATH, name):
    truecontent = []
    public = []
    str = ""
    with open(PATH, "r+") as fr:
        content = fr.readlines()
        fr.close()

    for lines in content:
        newline = lines.replace("\n", "")
        truecontent.append(newline)

    for publicacoes in truecontent:
        localanoautores = publicacoes.split("|")
        autores = localanoautores[2].split(",")
        for aut in autores:
            if name == aut:
                str = localanoautores[0] + "-" + localanoautores[1]
                public.append(str)
    return public


# print(ler(Path,"Barros"))
# coautor_todos(dicio)
def gera_cadeia(lista):
    newstr = ""
    charpos = []
    for i in lista:
        charpos.append(i[1])
    maxvalue = max(charpos)
    for i in range(maxvalue+1):
        #print(i)
        for ele in range(len(lista)):
            if i == lista[ele][1]:
                newstr += lista[ele][0] * (lista[ele][2] + 1)
    return newstr


lista = [('2', 1, 1), ('a', 10, 0), ('x', 0, 0), ('d', 3, 2), (' ', 6, 0), ('c', 7, 0), ('b', 8, 1)]
print(gera_cadeia(lista))
