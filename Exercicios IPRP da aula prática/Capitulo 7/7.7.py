import random
from turtle import *

ROOTORIGIN = "files/77.txt"


def criapares(ROOTORIGIN):
    content = f"{random.randint(1, 6)} {random.randint(1, 6)} \n"

    with open(ROOTORIGIN, "a", encoding="utf-8") as f:
        f.write(content)
        f.close()


def lerficheiroturtle(origin):
    with open(origin, "r") as fr:
        first_line = fr.readline()
        print(first_line)
        fr.seek(0)
        content = fr.readlines()
        fr.close()

    up()
    for lines in content:
        listcoords = lines.split(" ")
        print(listcoords)
        goto(int(listcoords[0])*25,int(listcoords[1])*25)
        down()



    fistcoords = first_line.split(" ")
    print(fistcoords)
    goto(int(fistcoords[0])*25,int(fistcoords[1])*25)
    print(pos())

criapares(ROOTORIGIN)
lerficheiroturtle(ROOTORIGIN)

done()
Terminator()
# for lines in listcoords:
#    listcoords = lerficheiroturtle(ROOTORIGIN).split(",", 1)  # para salvar so um elemento
# print(listcoords)
# print(listcoords[0], listcoords[1])
# goto(int(listcoords[0]),int(listcoords[1]))
# down()
