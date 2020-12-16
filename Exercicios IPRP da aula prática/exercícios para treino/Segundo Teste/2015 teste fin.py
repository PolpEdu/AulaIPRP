# 1
def func(l1, l2):
    for ele in l2:
        l1.append(ele)


list1 = [1, 2, 3]
list2 = [1, 2, 3]
func(list1, list2)
#print(func(list1, list2))
#print(list1)


# 2
def oc(string, ocorrencia):
    nvezes = 0
    for x in range(len(string)):
        for i in range(len(ocorrencia)):
            if x+i < len(ocorrencia):
                if string[x+i] == ocorrencia[i]:
                    if x+i == len(ocorrencia)-1:
                        nvezes += 1
    return nvezes


#print(oc("ollalal lal mundo", "lal"))

PATH = "files/vetores.txt"
def soma(PATH):
    truecontnent = []
    d = {}
    x = 0
    with open(PATH,"r") as fr:
        content = fr.readlines()
        fr.close()

    for x in content:
        x = x.replace("\n",
                      "")
        truecontnent.append(x)
    for vetores,ele in range(len(truecontnent)):
        print(vetores,ele)
        d["x"+str(vetores+1)] = x
    return d
print(soma(PATH))

