def filtra ( lista ):
    aux = []
    for elem in lista:
        if elem <= 0:
            return aux
        else:
            aux.append(elem)
    return aux

#print(filtra([1,2,3,4,-5]))

agenda = [( "08:00" ,"09:00" ,"DPalma" ) ,( "10:00" ,"11:00" ,"BRibeiro" ) ,( "13:00" ,"14:00" ,"ECosta" ) ,
           ( "17:00" ,"19:00" ,"TBaptista" ) ]

def periodos(agenda,dur):
    dict = {}
    disp = []
    starth = 0
    startm = 0
    for coisas in agenda:
        for x in range(coisas):
            print(coisas[x][:2])
            difh =int(coisas[x][:2])-0
            difm = int(coisas[x][4:])-0

            dict[coisas[2]] = [difh,difm]
            starth = coisas[x][1]

            disp.append((difh-0, difh))

    return disp
#faz esta merda caralho nao estou com paciencia vou estudar ED

print(periodos(agenda, "02:30"))