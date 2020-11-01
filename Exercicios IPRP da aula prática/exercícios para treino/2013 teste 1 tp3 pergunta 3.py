
def contagem(string):
    countera = 0
    counterb = 0
    for x in string:
        if x =='a':

            countera +=1
        elif x == 'b':

            counterb +=1
    #print(f"{countera} and {counterb}")
    if countera == counterb:
        print("O numero de As é igual ao numero de Bs")
    else:
        print("O numero de As é diferente do numero de Bs")

contagem('aaaaaaabbbbdsabb')