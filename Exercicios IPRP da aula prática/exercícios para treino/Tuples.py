#Tuples
#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

#os tuplos sao criados como tup=()
cad = 'ernesto'
cad[1] = 's'
#vai dar erro
#os elementos do tuplo têm referencias precisas na memoria, assim nao podem ser alteradas (até porque se pudessem podiam levar a erros)

tup = (1,2,3)
tup[0]= 4 #esta a dizer que os tuplos nao podem ser alterado e diz para mudar para uma list
#vai dar erro


t_1 = (1,2,3)
t_2 = t_1
t_3 = (1,2,3)
t_4 = (1,(1,2,3),4)
#e aqui criei um novo tuplo na memoria, não fui buscar a nenhum lado.
#ou
t_4 = (1,t_1,4)
#basicamente criei uma referencia aqui na memoria
a=2
b=4
id(t_4)
if id(t_1) == id(t_2):
    print(id(t_1))