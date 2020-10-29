# primeira forma
def forma1(stringINP):
    for x in stringINP:
        print(x)

# String é uma cadeia de caracteres, assim,
# x vai ser cada caracter da variavel string INP
# dou print a cada charater que a string contem.

def froma2(stringINP):
    for x in range(len(stringINP)):
        print(stringINP[x:x + 1])

# representar uma parte da string de cada vez tantas vezes como characteres a string tem.
# é diferente do primeiro metodo no sentido que na forma1, a string é vista como uma array de characteres
# aqui, na forma2, simplesmente escrevo uma parte da string de cada vez.
