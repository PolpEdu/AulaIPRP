PATH = "casais.txt"
PATHNOVO = "casaisNOVOS.txt"


def casais(PATH, nr):
    males = []
    females = []
    contentN = ""
    with open(PATH, "r") as f:
        content = f.readlines()
        #print(content)
        f.close()

    for line in content:
        line = line.replace("\n", "")
        print(line)
        dados = line.split(" ")  # ["TERESA", "F", "32"]
        if dados[1] == "F":
            females.append(dados)  # ["TERESA", "F", "32"]
        else:
            males.append(dados)

    # ex: [["TERESA", "F", "32"], ["Ines","F","17"], ["Patricia", "F", "18"]]
    casaislist = []
    print(females)
    print(males)
    for homens in males:
        for mulheres in females:
            dif = int(homens[2]) - int(mulheres[2])
            if dif < 0:
                dif = -1 * dif
            if dif < nr:

                contentN = "Casal: " + homens[0] + " " + mulheres[0] + "\n"
                if contentN in casaislist:
                    continue
                else:
                    with open(PATHNOVO, "a") as fr:
                        fr.write(contentN)
                        fr.close()
                    casaislist.append(contentN)

casais(PATH, 2)

def processa(string):
    vezes = 0
    finallist = []
    for x in range(len(string)):
        if string[x] not in finallist:
            if x + 1 > len(string) - 1:
                t = (string[x], x, vezes)
                finallist.append(t)
                break

            if string[x + 1] == string[x]:
                vezes += 1
            else:
                t = (string[x], x - vezes, vezes)
                finallist.append(t)
                vezes = 0
    return finallist

print(processa("x22ddd cbba"))