#Eduardo Nunes
def matrizinversa(matriz):
    for x in matriz:
        for y in range(len(x)):
            if x[y] == 1:
                x[y] =0
            else:
                x[y] =1
        print(x)

matrizinversa([[0,1,0],[1,1,1],[0,1,0]])
#https://codeshare.io/aJ9LPE