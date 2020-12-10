#Eduardo Nunes
ORIGIN = "files/711.txt"
from datetime import date

today = date.today()
d1 = today.strftime("%d/%m/%Y")

def escrever(ORIGIN,numerodavenda,Empresa,numerotelefone,data,montante,Vendedor):
    content = f"Venda a Dinheiro No {numerodavenda}\n" \
              f"-----------------------------------\n" \
              f"Empresa: {Empresa}\n" \
              f"N.C.:{numerotelefone}\n" \
              f"Data:{data}\n" \
              f"Valor:{montante}\n" \
              f"Vendedor: {Vendedor}\n"

    with open(ORIGIN, "w") as f:
        f.write(content)
        f.close()

nrV = input("Nr Venda: ")
Empresa = input("Empresa: ")
numerotelefone = input("Telefone: ")
data = d1
Valor = input("Valor: ")
Vendedor = input("Nome Vendedor: ")
escrever(ORIGIN,nrV,Empresa,numerotelefone,data,Valor,Vendedor)
print(f"Numero Venda:{nrV},\n"
      f"Empresa:{Empresa},\n"
      f"Numero de Telefone:{numerotelefone},\n"
      f"Data: {d1},\n"
      f"Valor: {Valor},\n"
      f"Vendedor: {Vendedor}.\n")
#https://codeshare.io/aydOp9