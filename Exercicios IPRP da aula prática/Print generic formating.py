import sys

# file = sys.sdout
print("Ola", "eu", "sou", "muito", "fixe")

# sep pode ser usefull
print("Ola", "eu", "sou", "muito", "fixe", sep="-", end=". ")  # para continuar na mesma linha o end=""

# Pode ser usefull
print('O primeiro nome é: %s e o último é: %s' % ('Ernestro', 'Costa'))
# Podemos criar strings sem concatenação.

print('%d' % 12.32)
print('%s' % 12.32)
print('%e' % 12.35, end="\n \n")

print('%.0f' % 12.34)
print('%.5f' % 12.34)
print('%10.2f' % 12.34)  # vai guardar espaco para 10 casas inteiras
print("%0.2f %10.2f" % (12.32, 12.34))  # vai guardar espaco para 10 casas inteiras

print('Eu sou {0}!'.format("toto"))

modelo2 = '{dorme}, {come} e {veste}'
texto21 = modelo2.format(come='mesa', veste='roupa lavada', dorme='cama')
print(texto21)
