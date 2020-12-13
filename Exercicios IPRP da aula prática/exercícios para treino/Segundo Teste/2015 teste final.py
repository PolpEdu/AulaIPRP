# Pergunta 1

# 2- (1,2,3)
a = 2
t = (1, 2, 3)


# t *2 = (1,2,3,1,2,3) o mesmo com listas.
def xpto(x, y):
    y = x * y
    return y


# print(xpto(a,t))

# Pergunta 2
def processa(str):
    l = []
    nvezes = 0
    for x in range(len(str)):
        if str[x] == str[x-1]:
            continue
        for char in str[x+1:]:
            if char == str[x]:
                nvezes += 1
            else:
                break

        l.append((str[x], x, nvezes))
        nvezes = 0
    return l


print(processa("x22ddd cbba"))

# Pergunta 3
d = {'pedro': ['rui', "dfsçjflksd"], 'rui': ['joao', "fdlksjfkls"], 'joao': ['rui', 'pedro', "fldkshfklsd"],
     "dfjkls": ["dsajk"]}


def dic(d):
    dict = {}
    list = []
    usrmaxi = ""
    maxi = 0
    for users in d.keys():
        l = len(d[users])
        dict[users] = l
        print(dict)
    for allusers in dict.keys():
        list.append(dict[allusers])
        maxi = max(list)
    for k, v in dict.items():
        if maxi == v:
            usrmaxi = k

    return usrmaxi, maxi

# print(dic(d))
