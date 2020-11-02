#Eduardo Nunes
a = 10
b = a
print(f"id(b):{id(b)} e id(a):{id(a)} são iguais aqui.")
a = 11
print(f"a: {a} id-{id(a)} || b: {b} id-{id(b)}")
print("As duas variaveis sao do tipo int. Se virmos a ordem das variaveis ao serem enunciadas conseguimos ver que "
      "a variavel b tem de valor 10, porque foi o unico valor que lhe foi correspondido e a variavel a 11 porque "
      "ela assumiu dois valores (10, onde se igualou a b e 11) e o ultimo valor que a assumiu na linha 4. \n"
      "Primeiramente a tinha o mesmo id que b mas depois como mudamos o seu valor, tem no final de tudo, um id diferente de b")
