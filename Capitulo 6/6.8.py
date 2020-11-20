# Eduardo Nunes

list = [[1, 0, 0], [0, 1, 1], [1, 0, 0]]


def apresentar(list):
    for x in list:
        print(x)


def rodar(matrix):
    for x in matrix:
        x1 = x[0]
        x2 = x[1]
        x3 = x[2]
        print(x1, x2, x3)

        matrix[0][2] = x3
        matrix[1][2] = x2
        matrix[2][2] = x1

    print(matrix)


apresentar(list)

rodar(list)
