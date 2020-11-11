#Eval()
entrada = eval(input("Quantos anos tens"))
print(entrada+1)

#e nao e preciso
entrada = int(input("Quantos anos tens"))
print(entrada+1)

#para evitar erros como:
#entrada = input("Quantos anos tens")
#print(entrada+1)

#o eval faz logo tudo o que queres quando nao sabes o input
entrada = eval(input("Qual e a tua altura"))
print(type(entrada), sep=" ",end='\n')