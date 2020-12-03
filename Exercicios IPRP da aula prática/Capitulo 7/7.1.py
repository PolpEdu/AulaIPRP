def create(mensagem):
    with open("files/primeiro.txt","w") as f:
        f.write(mensagem)
        f.close()
def read():
    with open("files/primeiro.txt", "r") as fr:
        string = fr.read()
        print(string)
        fr.close()

mensagem = "Acabei de criar o meu primeiro ficheiro em Python.\n"
create(mensagem)
read()
#https://codeshare.io/50Keol