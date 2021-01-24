x = 0


def locais(y):
    # print(x) x não esta defenido neste escopo
    x = 10
    print(x)
    print(y)


# print(y) y nao esta defenido neste escopo

def mist(seq):
    lista = []
    for i in range(len(seq), 0, -1):
        lista.append(sum(seq[len(seq) - i:]))
    return lista


# print(mist([1, 2, 3, 4, 5]))

from turtle import *
import math


def turtle(hora):
    horasmin = hora.split(":")
    horas = int(horasmin[0])
    minutos = int(horasmin[1])
    desenhar(horas, minutos)


pi = math.pi


def center():
    up()
    goto(0, 0)
    down()


def desenhar(horas, minutos):
    center()
    raio = 150

    seth(90)
    # horas
    horas = horas % 24
    g = 360 / 12
    right(g * horas)
    forward(raio * 6 / 7)

    center()

    # minutos
    seth(90)
    minutos = minutos % 60
    gm = 360 / (12 * 60)
    right(gm * minutos + g * horas)
    forward(raio * 4 / 7)

    center()
    circulo(raio)


def circulo(raio):
    up()
    seth(270)
    forward(raio)
    seth(0)
    down()
    circle(raio)


# turtle("7:50")


def comprar_vender(list):
    newlist = []
    media = 0
    for i in range(len(list)):
        soma = sum(list[:i + 1])
        maisum = i + 1
        media = soma / maisum
        if list[i] < media:
            newlist.append("c")
        else:
            newlist.append("v")
    return newlist


# print(comprar_vender([3, 4, 5, 7, 3, 5, 10, 13, 5, 7]))

import random

rede = {'tiago': ['rita', 'francisco', 'joao', 'filipa'], 'joao': ['tiago', 'ricardo'],
        'ricardo': ['rita', 'francisco'], 'rita': ['tiago', 'filipa', 'ricardo'], 'filipa': [], 'francisco': ['tiago']}


def sugestoes(nome, rede, nr):
    segtotais = []
    sug = []
    sugf = []
    for seguidores in rede[nome]:
        # tiago e ricardo
        for segdoseg in rede[seguidores]:
            segtotais.append(segdoseg)
    print(segtotais)
    for ele in segtotais:
        for ele2 in segtotais:
            if ele == ele2:
                if ele not in sugf:
                    sugf.append(ele)
                    continue
    for x in range(nr):
        choice = random.choice(sug)
        if choice not in sugf:
            sugf.append(choice)

    return sugf


print(sugestoes("joao", rede, 2))
