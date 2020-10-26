#demorei 5 minutos
def divisores(numero):
    ar =[]
    for x in range(1,numero+1):
        if numero % x ==0:
            ar.append(x)
    return ar

X = int(input("Numero: "))

print("Os seus divisores são: "+ str(divisores(X)))