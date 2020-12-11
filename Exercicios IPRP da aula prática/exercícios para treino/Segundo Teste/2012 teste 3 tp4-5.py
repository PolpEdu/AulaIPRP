# Pergunta 1

# Vai apresentar uma lista de todos os numeros em cada linha numa lista
# [[3] ,[2,500], [1], [2,12]]
l = 1
f = open('files/compras.txt')
l = [[int(x) for x in s.split() if x.isdigit()] for s in f.readlines()]

f.close()
# print(l)

# Pergunta 2
amigos = {'pedro': ['rui'], 'rui': ['joao'], 'joao': ['rui', 'pedro']}


def verdadeiros(string, d):
    for amigosdentro in d[string]:
        if string in d[amigosdentro]:
            return amigosdentro
    return []


print(verdadeiros("rui", amigos))

# Pergunta 3
PATH = "files/texto.txt"


def ler(PATH, n):
    string = ""
    with open(PATH, "r") as f:
        content = f.readlines()
        f.close()

    if len(content) <= n:
        print("FALTAM LINHAS")
        return

    for x in content[n]:
        string += x.upper()

    content[n] = string
    print(content)

    with open(PATH,"w") as f:
        for x in content:
            f.write(x)
        f.close()


#ler(PATH, 10)
