#Eduardo Nunes
import random
def percentagem(vezes):
    face = 6
    par = 0
    for x in range(vezes):
        saiu = random.randint(1,face)
        if saiu % 2 ==0:
            par+=1

    percentagem = par/vezes
    return percentagem
print(f"{percentagem(102200)*100} %")