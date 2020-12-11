# Pergunta 1
# O programa organiza as chaves do dicionario e depois adiciona numa lista a chave e o elemento que corresponde a chave por ordem.
# o QUE O PROGRAMA VAI APRESENTAR É :
# [(1006264, "ppp"),(1000043,"iprp"),(2000410,"trp"),(3000825,"cpr")]

# ou da erro porque a função sort não consegue ordernar dic.keys()
def sorted(x):
    x.sort()
    return x

dic = {1000043: "iprp", 2000410: "trp", 3000825: "cpr", 1006264: "ppp"}
lista = []
for i in sorted(dic.keys()):
    lista.append((i, dic[i]))
print(lista)

# Pergunta 2
d = {"XY2002": 10, "AY2011": 30, "ZX2001": 1000, "XY2010": 400, "XY2009": 40}


def quantidade(string, d):
    if len(string) != 6:
        return 0

    if string in d.keys():
        sum = 0
        for keyname in d.keys():
            if keyname[0] == string[0] and keyname[1] == string[1]:
                sum += d[keyname]
        return sum


# print(quantidade("XY2002",d))

# Pergunta 3º
PATH = "files/ficheiro.txt"


def ditado(PATH):
    dicionario = {}
    listapal = []
    contagem = 0
    with open(PATH, "r") as f:
        lido = f.readlines()
        f.close()

    for x in lido:
        x = x.replace("\n", "")
        listapal += x.split(" ")

    for _ in listapal:
        for palavra1 in listapal:
            dicionario[palavra1] = 0
            for palavra2 in listapal:

                if palavra1 == palavra2:
                    dicionario[palavra1] += 1
    return dicionario


print(ditado(PATH))
