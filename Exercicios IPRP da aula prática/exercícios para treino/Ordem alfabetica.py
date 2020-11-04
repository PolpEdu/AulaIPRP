def ordem(string):
    string = string.lower()
    for x in range(len(string)):
        if x == len(string)-1:
            return "Encontra-se por ordem"
        elif ord(string[x])>ord(string[x+1]):
            return "Não se encontra por ordem"


print(ordem("AABCDEEEEFFFGGGIJKLMNOPQRts"))