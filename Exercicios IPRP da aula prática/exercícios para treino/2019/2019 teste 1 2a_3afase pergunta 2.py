
def ola(string):
    newstring = ""
    for x in range(len(string) - 1):
        if x % 2 == 0:
            newstring += string[x + 1]
        else:
            newstring += string[x - 1]
        if len(string) % 2 == 1 and x == len(string) - 2:
            newstring += string[x + 1]
        elif len(string) % 2 == 0 and x == len(string) - 2:
            newstring += string[x]

    return newstring

print(ola("IBIZACARALHO"))
