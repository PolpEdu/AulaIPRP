import random

def numero(n):
    k=n
    for x in range(n):
        v = random.randint(1,100)
        if v > 50:
            k = k-1
    return k

print(numero(10000))