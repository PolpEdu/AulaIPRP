#Eduardo Nunes
import math

def CartesianaPolar(x, y):
    #Pelo teorema de pitagoras descobrimos o raio.
    r = math.sqrt(math.pow(x,2)+math.pow(y,2))

    #Descubro o teta atraves da funcao acos()
    teta = math.degrees(math.acos(x/r))

    return (round(r,2), round(teta,2))

x = int(input("coordenada X: "))
y = int(input("coordenada Y: "))


print("As coordenadas Polares são: "+ str(CartesianaPolar(x, y)))