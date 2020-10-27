import random
#nestes exercicios feitos no notepad nao esquecer de fechar parenteses
#e transformar em strings as ints!!!
nr = 0
soma = 0
y = int(input("Quantos dados deseja jogar? "))

for x in range(y):
    jogada = random.randint(1, 6)
    print(jogada)
    if jogada == 6:
        nr += 1
    soma = soma + jogada

print(soma)
print("A soma foi de " + str(soma) + "\nE o numero seis saiu " + str(nr) + " vezes")