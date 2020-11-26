# Eduardo Nunes
def posicoes(string):
    dictionary = {'a':[],'e':[],'i':[],'o':[],'u':[], 'A':[], 'E':[], 'I':[],'O':[],'U':[]}
    pos = []
    vogais= ['a','e','i','o','u','A','E','I','O','U']

    for x in range(len(string)):
        if string[x] not in vogais:
            continue

        dictionary.get(string[x]).append(x)

    for x in list(dictionary.keys()):
        if not dictionary.get(x):
            dictionary.pop(x)


    print(dictionary)


posicoes('agora e que vao ser elas, Ai, Ai, OUEI!')
#https://codeshare.io/5OnDlW