# Eduardo Nunes
# Este metodo de encriptação chama-se "Ceasar Cipher"
import math

alfabeto = "abcdefghijklmnopqrstuvwxyz"


def CeaserCipherENCRIPT(string, distancia):
    encripted = ""
    distancia = distancia - 26 * math.floor(distancia / 26)
    for x in string:
        xlower = x.lower()
        if xlower in alfabeto:
            lugar = alfabeto.index(xlower)
            newpos = lugar + distancia
            if newpos >= 26:
                overflow = newpos - 26
                if x.isupper():
                    encripted += alfabeto[overflow].upper()
                else:
                    encripted += alfabeto[overflow]
            else:
                if x.isupper():
                    encripted += alfabeto[newpos].upper()
                else:
                    encripted += alfabeto[newpos]
        else:
            encripted += x

    return encripted


def CeaserCipherDECRIPT(string, d):
    # e so ir para o lado oposto
    return CeaserCipherENCRIPT(string, -d)


# NOVO METODO aquele (ord)
# mas nao da para converter para simbolos...
# dar dá mas tinhas que fazer muitas exceções.
def encriptORD(string, d):
    newstring = ""
    d= d - 26 * math.floor(d / 26)
    for x in string:
        newchar = ord(x) + d
        if ord('a') <= ord(x) <= ord('z') or ord('A') <= ord(x) <= ord('Z'):
            if ord('a') <= newchar <= ord('z') or ord('A') <= newchar <= ord('Z'):
                newstring += chr(newchar)
            else:
                newchar = newchar-26
                newstring += chr(newchar)
        else:
            newstring += x
    return newstring


def decriptORD(string, d):
    return encriptORD(string, -d)


str = "According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground."
print(CeaserCipherENCRIPT(str, 46))
print(encriptORD(str,46))

strenc = "Uwwilxcha ni uff ehiqh fuqm iz upcuncih, nbyly cm hi qus nbun u vyy mbiofx vy uvfy ni zfs. Cnm qcham uly nii mguff ni ayn cnm zun fcnnfy vixs izz nby aliohx."
print(CeaserCipherDECRIPT(strenc, 46))
print(decriptORD(strenc,46))
