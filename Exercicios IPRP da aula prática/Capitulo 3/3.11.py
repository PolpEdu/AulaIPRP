# Eduardo Nunes

# regra de emparelhamento de bases
# alfabeto de 4 letras
# iterar sobre estas letras

# a string terá estas 4 letras e é só substituir
# A - T
# T - A
# G - C
# C - G

#Eu tentei fazer replace, mas era muito pouco eficiente
#visto que dava replace a todos as characters.
#Assim, criar uma nova string com letras corretas nos sitios corretos
#parece muito mais eficiente.
def adn(string):
    # primeiro vou ver se é valida
    newstring = ""
    string = string.upper()
    #Vou ignorar letras que nao sao A,T,G ou C.
    for x in string:
        if x == "A":
            newstring += "T"
        elif x=="T":
            newstring += "A"
        elif x == "G":
            newstring += "C"
        elif x =="C":
            newstring += "G"
    return newstring


x = str(input("String: "))
print(adn(x))
