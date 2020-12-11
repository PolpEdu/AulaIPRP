# Pergunta 1
# 1-tirar o range porque assim aparece o nr e nos queremos a letra.
# 2-tirar o .upper e fazer
# if car == letra or car == letra.upper para contar os dois casos
# 3- em vez de fazer num = 1 fazer num+=1 para adicionar e nao meter sempre um

# Pergunta 2
def mdc(divisores1, divisores2):
    newlist = []
    for ele1 in divisores1:
        for ele2 in divisores2:
            if ele1 == ele2:
                newlist.append(ele1)

    return max(newlist), newlist


# print(mdc([1, 2, 4, 8], [1, 2, 3, 4, 6, 12]))
import math


# Pergunta 3
def divide(string, divisao):
    cadadiv = len(string) / divisao  # mais um do resto..
    cadadiv = math.ceil(cadadiv)
    print(cadadiv)
    newstr = ""
    total = []

    for ele in range(len(string)):
        newstr += string[ele]
        if len(newstr) == cadadiv:
            total.append(newstr)
            newstr = ""

    if len(newstr) != 0:
        total.append(newstr)

    return total


print(divide("123456789", 4))
