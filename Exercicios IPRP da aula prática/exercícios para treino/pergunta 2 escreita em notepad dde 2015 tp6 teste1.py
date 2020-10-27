import math

#CUIDADO DO RANGE DO FOR IN A VARIAVEL N NUNCA CHEGA A SER 10!!!!!!!!

def maiores_90_circulo(n1, n2):
    print("Poligonos com area maior do que 90% da area do circulo:\n")
    r = 1
    pi = math.pi
    for n in range(n1, n2+1):
        # para n = 4
        areapoligono = n * (math.cos(pi / n)) * (math.sin(pi / n))
        # areapoligono = 2
        areacirculo = pi * (r ** 2) - areapoligono
        # areacirculo = pi-2

        proporcao = areacirculo / areapoligono
        print(str(n) + " de n : " + str(proporcao))
        # proporcao = (pi-2)/2 =0.57

        if proporcao < 0.1:
            print("Poligono com " + str(n) + " lados")


maiores_90_circulo(3, 10)