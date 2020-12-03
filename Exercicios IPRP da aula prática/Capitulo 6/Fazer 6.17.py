D = {"joao": 18, "pedro": 18, "tiago": 13, "luis": 18}
def inverter(dicionario):
    D_inv = {}
    for k, v in dicionario.items():
        D_inv[v] = D_inv.get(v, []) + [k]  # adiciona a chave k como um elemento na D_invertida,

    print(D_inv)
inverter(D)
#https://codeshare.io/5g7vVR