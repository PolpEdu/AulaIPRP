# Pergunta 2
lista = ["isto e um teste!!", "nao e facil ser informatico.",
         "realmente custa programar...",
         "mas... nada e facil hoje em dia."]
posicoes = [2, 3, 0, 2]


def ok(lista, posicoes):
    str = ""
    for ele in lista:
        str += ele.split(" ")[posicoes[lista.index(ele)]] + " "
    newstr = str[:len(str) - 1]
    newstr += "."

    return newstr


res = ok(lista, posicoes)
print(res)
