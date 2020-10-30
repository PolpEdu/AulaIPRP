# Eduardo Nunes

# Este metodo de encriptação chama-se "Ceasar Cipher"
alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabetoarr = list(alfabeto)


def CeaserCipherENCRIPT(string, distancia):
    encripted = ""
    for x in string:
        xlower = x.lower()
        if xlower in alfabeto:
            lugar = alfabeto.index(xlower)

            newpos = lugar + distancia
            #print(f"{lugar } ---- {newpos}")
            #print(x)
            if newpos >= 26:
                overflow = newpos - 26
                if x.isupper():
                    encripted += alfabetoarr[overflow].upper()

                else:
                    encripted += alfabetoarr[overflow]
            else:
                if x.isupper():
                    encripted += alfabetoarr[newpos].upper()
                else:
                    encripted += alfabetoarr[newpos]
        else:
            encripted += x

    return encripted


def CeaserCipherDECRIPT(string, d):
    # e so ir para o lado oposto
    return CeaserCipherENCRIPT(string, -d)


str = "According to all known laws of aviation, there is no way that a bee should be able to fly."
print(CeaserCipherENCRIPT(str,2))

strenc = "Ceeqtfkpi vq cnn mpqyp ncyu qh cxkcvkqp, vjgtg ku pq yca vjcv c dgg ujqwnf dg cdng vq hna."
print(CeaserCipherENCRIPT(strenc, -2))
