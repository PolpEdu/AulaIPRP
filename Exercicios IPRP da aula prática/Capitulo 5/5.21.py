#Eduardo Nunes
string = "Eduardo"

a = string.find('a')
print(a)
a2 = string.find('P')
print(a2)

b = string.index('a')
if b == 3:
    print(b)

try:
    c = string.index('P')
    if c == -1:
        print(c)
except:
    print("-1")

