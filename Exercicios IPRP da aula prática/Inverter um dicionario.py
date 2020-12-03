# Eduardo

###################### PARA INTEGERS!!! #######################
D = {"joao": 18, "pedro": 18, "tiago": 13, "luis": 18}
D_inv = {}
for k, v in D.items():
    # crio no novo dicionario invertido, todos os nomes opostos
    # D_inv[v] escreve as chaves agora como elementos

    # D_inv.get(x,[])+[x] escreve os elemntos (antes chaves) no lugar correto
    D_inv[v] = D_inv.get(v, [])
    D_inv[v].append(k)

    # D_inv = {value: key for (key, value) in D.items()}
    # mas so com este codigo nao conseguimos ter 2 18s por exemplo.
    # so da para valores unicos

    # para valores nao unicos:

print(D_inv)

################### PARA LISTAS ITERAVEIS ########################
D = {'joao': ['IPRP', 'MAT', 'BIO'], 'pedro': ['IPRP', 'TI'], 'tiago': ['MAT']}
D_inv = {}
for k, v in D.items():
    # onde k sera a chave
    # e v sera o valor dessa chave
    for elem in v:
        # vou iterar por todos os elementos
        # e tomá-las como novas chaves
        D_inv[elem] = D_inv.get(elem, []) + [k]  # adiciona a chave k como um elemento na D_invertida,
        # fazemos D_inv.get(elem, []) para adicionar as anteriores que ja estavam no dicionario

print(D_inv)
# agora temos que as chaves contem os nomes
