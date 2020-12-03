#  "files/primeiro.txt"

def coping(ROOTORIGIN,PATHORIGIN,Name):
    with open(ROOTORIGIN, "r") as f:
        content = f.read()
        f.close()

    TARGETPATH = PATHORIGIN + "/" + Name
    with open(TARGETPATH, "w", encoding="utf-16") as fr:
        fr.write(content)
        fr.close()

PATH = input("Qual o ficheiro de origem?\n")
PATHORIGIN = input("Onde criar o ficheiro?\n")
NAME = input("Qual o nome?\n")
coping(PATH, PATHORIGIN, NAME)
#https://codeshare.io/2WnbV8