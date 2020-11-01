
def acumula_letras(string, ficar):
    newstring = ''
    for x in string:
        if x in ficar:
            newstring += x
    return newstring

string1 = acumula_letras('o teste deste exercicio', 'eo')
string2 = acumula_letras('o teste deste exercicio', 'oi')
print(string1)
print(string2)