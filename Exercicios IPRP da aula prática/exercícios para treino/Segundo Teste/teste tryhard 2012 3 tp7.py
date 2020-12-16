# pergunta 1
# ? -- 4,5,5,3,7,5
# ? -- 7

# pergunta 2
def fre(string):
    oco = {}
    counter = 0
    list = string.split(" ")
    list = sorted(list)
    for palavra1 in list:
        counter = 0
        for palavra2 in list:
            if palavra1 == palavra2:
                counter += 1
        oco[palavra1] = counter
    return oco


# print(fre("OLA OLA OLA OLA EDUARDO OLA EDUARDO FIXE ZEBRA AGUIA"))

# pergunta 3
PATH = "files/estatisticas.txt"


def acres(PATH):
    truecontent = []
    difs = {}
    difsl = []
    stri = ""
    with open(PATH, "r") as f:
        content = f.readlines()
        f.close()

    for lines in content:
        newline = lines.replace("\n", "")
        truecontent.append(newline)

    for ele in truecontent:
        equipap = ele.split(",")
        if int(equipap[2]) - int(equipap[1]) < 0:
            dif = int(equipap[2]) - int(equipap[1])
        else:
            dif = int(equipap[2]) - int(equipap[1])
        difs[equipap[0]] = dif

    for k, v in difs.items():
        difsl.append(v)

    maxval = max(difsl)
    for k, v in difs.items():
        if v == maxval:
            stri = "\n" + k + ", " + str(v)

    with open(PATH, "a+") as fa:
        fa.write(stri)
        fa.close()


acres(PATH)
