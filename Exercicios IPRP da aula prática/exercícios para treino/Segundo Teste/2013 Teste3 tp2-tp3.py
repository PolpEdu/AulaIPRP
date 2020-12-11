# Pergunta 1:
# primeiro vai ler o e depois ai ler iro.

f = open("files/texto.txt", "r")
f.seek(-2, 2)
print(f.read(1))

f.seek(-2, 1)
print(f.read())


# print(cont)

# pergunta 2:
def conta(list):
    dict = {}
    for palavra in list:
        dict[palavra] = 0
        for palavra2 in list:
            if palavra == palavra2:
                dict[palavra] += 1
    return dict


# print(conta(["um","dois", "tres", "dois", "dois", "quatro", "um"]))

# Pergunta 3
PATH = "files/texto.txt"


def pergunta(PATH, n):
    with open(PATH, "r") as f:
        content = f.readlines()
        f.close()

    for x in content:
        x = x.replace("\n", "")

    lits = x.split(" ")
    if n > len(lits):
        return ""
    return lits[n - 1]


print(pergunta(PATH, 5))
