#Eduardo Nunes
import math

def calculo(peso, altura):
    imc = peso/(math.pow(altura, 2))
    return imc
peso = int(input("Qual é o seu peso em kg?\n"))
altura = int(input("Qual é a sua altura em metros?\n"))

print("O seu Indice de massa corporal é", calculo(peso,altura))