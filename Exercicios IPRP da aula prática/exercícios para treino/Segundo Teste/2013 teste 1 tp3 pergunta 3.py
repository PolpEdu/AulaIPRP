f = open("files/texto.txt", "r")
f.seek(-2, 2)
cont = f.read(1)
print(cont)

f.seek(-2, 1)
cont2 = f.read()
print(cont)
