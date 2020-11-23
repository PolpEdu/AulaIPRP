# Eduardo Nunes
list = [[1, 0, 0], [0, 1, 1], [1, 0, 0]]


def apresentar(list):
    for x in list:
        print(x)


def rodar(matrix):
    novamatriz = []
    for x in range(len(matrix[0])):
        novalista = []
        for y in matrix:
            novalista.append(y[x])
        novamatriz.append(novalista)

    for i in novamatriz:
        print(i)

apresentar(list)
print("")
rodar(list)
#https://codeshare.io/axl0kk
