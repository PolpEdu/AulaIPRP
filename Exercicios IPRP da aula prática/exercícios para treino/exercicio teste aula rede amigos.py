# Rede amigos aula
PATH = "files/amigos.txt"


# Vou fazer desta forma
# P1 P2 P3 P4
# P2 P1 P3 P4
# a PRIMIERA da o user e o restante os amigos
# repete amizades :(((


# Podia fazer desta:
# P1 P2
# P1 P3
# P1 P4
# P2 P1
# Ainda repete amizades

# OU A MELHOR FORMA para economizar data:
# P1 P2 P3 P4
#  0  1  1  1 P1
#     0  1  1 P2
#        0  1 P3
#           0 P4

# UMA MATRIZ de pessoas
# MAS e uma forma ma, a matriz cresce de forma quadratica, se ninguem fosse amigo E HOUVESSE 100000 AMIGOS
# a matriz ERA UMA MATRIZ ENORME para guardar basicamente nada.

# a melhor maneira seria a primeira que eu fiz

# ficheiro temos liberdade
# dicionario ={pessoa: [amigos]}
# {P1:[P2,P3,P4], P2:[P1,P3,P4]}

def Readamigos(PATH):
    d = {}
    userseAmigoslist = []
    contentlist = []
    with open(PATH, "r+") as fr:
        content = fr.readlines()
        fr.close()

    for line in content:
        newline = line.replace("\n", "")
        contentlist.append(newline)

    for line in contentlist:
        userseAmigos = line.split(",")
        userseAmigoslist.append(userseAmigos)

    for nomes in userseAmigoslist:
        mainuser = userseAmigoslist[userseAmigoslist.index(nomes)][0]
        d[mainuser] = userseAmigoslist[userseAmigoslist.index(nomes)][1:]  # tiro o primeiro que e o user

    # primeiro ele user, elles a seguir amigos, todos separados por virgulos, separados por linhas cada user
    return d


def write(PATH):
    with open(PATH, "a+") as f:
        f.write("\n" + str(Readamigos(PATH)))
        f.close()


NEWPATH = "files/eduardosuperfixe.txt"


def writeinfiledict(d, PATH):
    for k, v in d.items():
        print(v)
        content = str(k) + ": " + str(v) + "\n"
        with open(PATH, "a+") as f:
            f.write(content)
            f.close()


def addamigos(list, PATH):
    liststr = "\n" + ", ".join(list)

    with open(PATH, "a") as f:
        f.write(liststr)
        f.close()

    return list


def checkamizadesprof(PATH, friend1, friend2):
    # para ver o quanto estao relacionados amizades
    d = Readamigos(PATH)
    # print(d)
    for k, v in d.items():
        if k == friend1:
            # v is friends of friend1 here.
            for friends in v:
                # getting the amigos of friends of friends1
                for k1, v1 in d.items():
                    if k1 == friends:
                        print(v1)
                        for newfriends in v1:
                            if newfriends == friend2:
                                print(f"{friend1} - {newfriends} - {friend2}")
#quase ja esta quase

checkamizadesprof(PATH, "Pedro", "Paulo")
# write(PATH)
# writeinfiledict(amigos(PATH),NEWPATH)
# addamigos(["Alvaro", "Carlos"],PATH)
