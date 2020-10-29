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
            # print(lugar)
            if lugar + distancia > 26:
                overflow = 26 - lugar
                if x.isupper():
                    encripted += alfabetoarr[overflow].upper()
                else:
                    encripted += alfabetoarr[overflow]
            else:
                if x.isupper():
                    #print(lugar+distancia)
                    encripted += alfabetoarr[lugar + distancia].upper()
                else:
                    print(lugar+distancia)
                    encripted += alfabetoarr[lugar + distancia]
        else:
            encripted += x

    return encripted


def CeaserCipherDECRIPT(string, d):
    # e so ir para o lado oposto
    return CeaserCipherENCRIPT(string, -d)

str = "According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground."
print(CeaserCipherENCRIPT(str, 2))

strenc = "Cddpsejoh up bmm lopxo mbxt pg bwjbujpo, uifsf jt op xbz uibu b cff tipvme cf bcmf up gmz. Kut xjoht bsf upp tnbmm up hfu jut gbu mjuumf cpez pgg uif hspvoe."
#print(CeaserCipherENCRIPT(strenc, -2))
