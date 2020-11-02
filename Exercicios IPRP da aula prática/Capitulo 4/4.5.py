#Eduardo Nunes
x = 5
print(id(x))
x = x+1
print(id(x))

print("x tera sempre o mesmo tipo, no entanto,  terá valores e ids diferentes visto que apesar de somar a x,"
      "o proprio x mais um, estou a criar uma nova instancia de x e portanto terão ids diferentes mesmo somando a mesma"
      "variavel.")