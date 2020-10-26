# Eduardo Nunes
vogais = ["a", "e", "i", "o", "u"]

def substituir(string):
    string = string.lower()
    for x in string:
        #print(x)
        if x in vogais:
            string = string.replace(x, " ")

    return string


x = str(input("Diz uma frase: "))
print(substituir(x))
