palavra_original = "domino"
import random

def palavra_aleatoria(string):
    newstring = ""
    for x in string:
            numerorandom = random.randint(0,len(string)-1)
            #print(numerorandom)
            newstring += string[numerorandom]

    return newstring

print(palavra_aleatoria(palavra_original))