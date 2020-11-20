#Os dicionários permitem fazer associações entre objetos

#nao garantem ordem de acordo com a "chave-valor"

bases = {'A':'Adenina', 'C':'Citosina','T':'Timina','G':'Guanina'}
#O QUE ESTA À ESQUERDA É A CHAVE E A DIREITA É O VALOR
#Chave:Valor,Chave:Valor,Chave:Valor

#todas as chaves tem que ser distintas
#São tambem obejtos:

id(bases)
type(bases)
#são mutaveis.


#Dicionario vazio:
dicio_vaz = dict()
print(dicio_vaz)

meu_dicio = dict({'nome':'ernesto','altura':1.81})
print(meu_dicio)
#ou
meu_dicio2 = dict(nome='ernesto',altura=1.81) #altura vai ser float
print(meu_dicio2)

#mapeamentos, não sequencias, heterogeneos, mutaveis

#como acessar?
print(meu_dicio2['nome'])
print(bases['A'])
print(bases['C'])

#chaves são unicas
dicio={'A':'Adenina',2:'dois','bases': ['A','C','T','G'],5+4.5j:'complex'}
print(dicio)
dicio.setdefault('3','tres')
print(dicio) #se nao existir adiciona
dicio.setdefault('bases','BASES')
print(dicio) #se existir muda

#juntar dois dicionarios:
meu_dicio.update(meu_dicio2)
print(meu_dicio) #nao muda nada no dicio2

#para remover uma entrada:
print(meu_dicio2)
del meu_dicio2['nome']
print(meu_dicio2)


#eliminar todo
del dicio_vaz
#print(dicio_vaz) dá erro porque limpa o nome tambem

#limpar o que esta la dentro
#dicio.clear()
#print(dicio)

#limpar so 1
print(meu_dicio)
meu_dicio.pop('altura')
print(meu_dicio)

meu_dicio = meu_dicio2.copy()
print(meu_dicio.items())
print(meu_dicio.keys())
print(meu_dicio.values())
Tru = 'A' in dicio
print(Tru)

print(dicio.get('bases'))

for c in dicio.keys():
    print(c)

#IMPORTANTE:

#dicionario em compreensao
dicio = {chave:valor for (chave,valor) in zip(['c','b','a'],[1,2,3])} #DEFENIR UM DICIONARIO POR COMPREENSAO!
#ha maneiras que da para dar sort nao vi, ver na aula
print(dicio)

print("")

for c,v in dicio.items():
    #a chave vai ficar associado a c e o item vai ficar associado a v
    print('d[',c,']=',v)

