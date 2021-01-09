# pergunta 2
dic = {"joao": [(100, 4, 5), (200, 3, 4)], "maria": [(101, 4, 5)], "carlos": [(200, 3, 4)]}


def search_location(d, x, y):
    for k, v in d.items():
        for pos in v:
            #print(pos)
            if pos[1] == x and pos[2] == y:
                print(f"As {pos[0]}h, {k} esteve em {(pos[1], pos[2])}")


search_location(dic, 4, 5)

# pergunta 3
PATH = "dados.txt"

dic = {"joao": [(100, 4, 5), (200, 3, 4)], "maria": [(101, 4, 5)], "carlos": [(200, 3, 4)]}

def exportloc(dic, PATH):
    content = ""
    for k, v in dic.items():
        for pos in v:
            content += k + "," + str(pos[0]) + "," \
                       + str(pos[1]) + "," + str(pos[2]) + "\n"
            print(content)


    f = open(PATH, "w+")
    f.write(content)
    f.close()

    with open(PATH, "w+") as f:
        f.write(content)
        f.close()

#exportloc(dic,PATH)
