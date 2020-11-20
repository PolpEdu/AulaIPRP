# Eduardo Nunes

def padraoA(size):
    for x in range(1, size + 1):
        for y in range(1, x + 1):
            print(f"{y} ", end="")
        print("")
    return


def padraoB(size):
    for x in range(size, 0, -1):
        for y in range(1, x+1):
            print(f"{y} ", end="")
        print("")


def padraoC(size):
    for x in range(0,size+1):
        for i in range(size-x):
            print("  ",end="")
        for y in range(x, 0,-1):
            print(f"{y} ",end="")
        print("")

def padraoD(size):
    for x in range(0,size+1):
        for i in range(size-x):
            print(" ",end="")
        for y in range(x, 0,-1):
            print(f"{y} ",end="")
        print("")

padraoA(5)
padraoB(5)
padraoC(5)
padraoD(5)