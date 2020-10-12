#Eduardo Nunes
import math

def RazaoParaProtestar(HamburguerAntigo, hamburguerNovo):
    AreaNova = math.pow(hamburguerNovo, 2)
    #print(AreaNova)
    AreaAntiga = math.pi * math.pow(HamburguerAntigo,2)
    #print(AreaAntiga)

    if AreaAntiga > AreaNova:
        return True
    else:
        return False

if RazaoParaProtestar(8.89,7.62) == True:
    print("Tenho razões para protestar!!!!")
else:
    print("Não tenho razões para protestar...")
