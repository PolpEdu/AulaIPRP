# Eduardo Nunes
arvergeneologica = {
    'Pais-Antunes': ['PAULO'],
    'Pais-Nunes': ['CARLOS', 'PEDRO', 'FERNANDO'],
    'Pais-Gonçalves': ['TOMAS', 'JÚLIO', 'ERNESTO', 'BRUNO'],
    'Pais-Freitas': ['TIAGO', 'CARLOTA', 'BÁRBARA', 'FRANCISCA', "CARLOTA"]
}

#fazer tambem com netos
def arvore(arvoregene, nome1, nome2):
    for nome1, pais1 in arvoregene.items():
        for nome2, pais2 in arvoregene.items():
            if pais1 == pais2 and nome1 != nome2:
                print("São irmaos: ", end="")
                print(nome1, pais1)
                print(nome2, pais2)


# nao funciona nao sei porque
arvore(arvergeneologica, 'CARLOS', 'PEDRO')
