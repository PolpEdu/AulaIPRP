def divisores(numero):
    for x in range(1,numero+1):
        if numero % x == 0:
            print(f"O numero e divisivel por: {x}")

divisores(100)