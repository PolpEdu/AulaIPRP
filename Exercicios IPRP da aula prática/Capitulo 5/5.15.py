# Eduardo Nunes

# aproximar o numero e através da expressao
infinito = 1000

def fatorial(i):
    y = 1
    if i == 0:
        return 1
    for x in range(1, i + 1):
        y = x *y
    return y

def e():
    e = 0
    for i in range(infinito):
        e = 1/fatorial(i) + e
    print(e)

e()