#Eduardo Nunes
def escrever(stringI):
    print(stringI[2:4])
    for x in range(1, len(stringI)+1):
        print(stringI[:x])
        #fazer print(stringI[0:x] ou print(stringI[:x]) é igual.

    #newstring = ""
    #for x in stringI:
    #    newstring +=x
    #    print(newstring)

escrever("Hello")