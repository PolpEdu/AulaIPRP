#Eduardo Nunes

#kg,preço-compra/kg,stock,preco-venda/kg
frutaPreco = {
    "bananas":[1200, 0.40,400,0.99],
    "maças":[2500,1.20,200,1.99],
    "peras":[300,0.70,250,1.99],
    "goiabas":[100,5.00,40,11.73]


}
def lucro(frutaPreco):
    for x in frutaPreco.keys():
        frutacompradacliente = frutaPreco[x][0]-frutaPreco[x][2]

        profit = round(frutacompradacliente*frutaPreco[x][3])

        gasto = round(frutaPreco[x][0]*frutaPreco[x][1])

        total = profit-gasto
        print(f"Total em {x}: {total}€, ou {round(total/100)}% de lucro")

def maiscara(frutaPreco):
    lista=[]
    listacompra=[]
    for x in frutaPreco.keys():
        lista.append(frutaPreco[x][3])
        listacompra.append(frutaPreco[x][1])

    print(f"O preço máximo de venda é {max(lista)} e o preço máximo de compra é {max(listacompra)}.")

lucro(frutaPreco)
maiscara(frutaPreco)
#https://codeshare.io/2pX7OE