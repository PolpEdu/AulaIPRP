import datetime


def adddate(PATH):
    with open(PATH, "a", encoding="utf-16") as f:
        today = datetime.date.today()
        todaystrformatted = today.strftime("%d/%m/%Y")
        f.write("E hoje é: "+str(todaystrformatted))
        f.close()

#ou
def adddate2(PATH):
    with open(PATH, "r+", encoding="utf-16") as f:
        f.seek(0,2)
        today = datetime.date.today()
        todaystrformatted = today.strftime("%d/%m/%Y")
        f.write("E hoje é: "+str(todaystrformatted))
        f.close()

adddate("files/primeiro.txt")


def read(PATH):
    with open(PATH, "r") as f:
        print(f.read())
        f.close()


read("files/primeiro.txt")
# https://codeshare.io/G63oyg
