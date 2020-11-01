# Eduardo Nunes
# Este metodo de encriptação chama-se "Ceasar Cipher"
import math

alfabeto = "abcdefghijklmnopqrstuvwxyz"

def CeaserCipherENCRIPT(string, distancia):
    encripted = ""
    distancia = distancia - 26 * math.floor(distancia/26)
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

str = "According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground."
print(CeaserCipherENCRIPT(str,2))

strenc = "Ceeqtfkpi vq cnn mpqyp ncyu qh cxkcvkqp, vjgtg ku pq yca vjcv c dgg ujqwnf dg cdng vq hna. Kvu ykpiu ctg vqq uocnn vq igv kvu hcv nkvvng dqfa qhh vjg itqwpf."
print(CeaserCipherENCRIPT(strenc, -2))
