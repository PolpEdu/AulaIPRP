def acronimo(stri):
    newstring = ""
    for x in range(len(stri)):
        if x == 0:
            newstring += stri[x]
        if stri[x] == " ":
            newstring += stri[x + 1]
        # a letra a seguir

    return newstring.upper()


print(acronimo("Hello My Name is Eduardo"))
