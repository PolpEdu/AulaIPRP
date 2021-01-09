def f(str):
    contera = 0
    conterr = 0
    list = str.split("c")
    print(list)
    for x in list:
        if x == "a":
            contera += 1
        if x == "r":
            conterr += 1
    print(contera, conterr)
f("cacrcrcrcacacacacrcrcrcacacrcacacrcacr")