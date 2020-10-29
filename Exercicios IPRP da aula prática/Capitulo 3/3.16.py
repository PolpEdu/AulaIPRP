def escrever(string):
    y = len(string)
    for x in range(1, len(string) + 1):
        print(string[y - x:y])
        # criar uma new string e ir adicionando e dando print aos characteres tambem dava
        #mas preciso de a inverter e nao e bom isso...
        # mais bonito


#escrever("Hello")


# ouuuuu
def escrever2(string):
    y = len(string)
    for x in range(len(string) - 1, -1, -1):
        # fazer um for loop backwards, o incremento e o parametro final do range.
        # fica feio.
        print(string[x:y])


escrever2("Hello")
