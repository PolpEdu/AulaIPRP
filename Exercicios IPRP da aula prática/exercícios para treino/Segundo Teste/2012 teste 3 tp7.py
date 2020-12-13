#Pergunta
lista = [ x + y for x in [1 ,2 ,4] for y in [3 ,1 ,4]if x != y ]
#print(lista)
#print(*lista)
#Pergunta 2
def text(string):
    initiallist = []
    dictoc= {}
    nvezes = 0
    listpal = string.split(" ")
    listpal = sorted(listpal) #organizo a lista antes
    for x in listpal:
        for i in listpal:
            if x == i:
                nvezes +=1
        dictoc[x] = nvezes
        nvezes = 0

    return dictoc
#print(text("OLA EDUARDO EDUARDO EDUARDO URSA URSA URSA BOI WTF ALOOOOO BABY THE TREASURE IS IN MY ROOM ROOM IN MY"))

#pergunta 3
PATH = "files/estatisticas.txt"
import math

def acres(PATH):
    dict ={}
    list = []
    newlist = []
    scores = []
    name = ""
    with open(PATH,"r+") as f:
        cont = f.readlines()
        f.close()

    for e in cont:
        e = e.replace("\n","")
        list.append(e)
    
    for equip in list:
        newlist.append(equip.split(","))

    print(newlist)
    for ele in newlist:

        dif = int(ele[1])-int(ele[2])
        if dif< 0:
            dif *= -1
        dict[ele[0]] = dif

    for k,v in dict.items():
        scores.append(v)

    maxi = max(scores)
    for k,v in dict.items():
        if v == maxi:
            name = k

    total = "Maior diferença: "+ str(name) + ":" +str(maxi)
    with open(PATH,"a") as fr:
        fr.write(total)
        fr.close()

acres(PATH)