def func(v,a,b):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    w = ""
    lugara = alfabeto.index(a)
    lugarb = alfabeto.index(b)

    for x in v:
        lugarx = alfabeto.index(x)
        if lugara <= lugarx <= lugarb:
            w += x
    return w

print(func("fgze","d","f"))