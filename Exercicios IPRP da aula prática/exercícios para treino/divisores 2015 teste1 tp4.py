def divisores(numero):
    if numero <=0:
        return
    for x in range(1,numero+1):
        # vai ser de 1 a 10
        if (numero % x) == 0:
            print(f"O número é divisivel por {x}")

divisores(50)
