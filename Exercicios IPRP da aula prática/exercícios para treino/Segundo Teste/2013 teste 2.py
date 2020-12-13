# Pergunta 2
import math


def g(x):
    res = 0
    for i in range(100):
        res = math.pow(-1, i) * round(((math.pow(x, i)) / math.factorial(i)), 0.001)
    return res
#fazert este teste, n tenho paciencia

print(g(1))
