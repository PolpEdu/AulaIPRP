def tabuada(numero):
    print(f"Tabuada do numero {numero} \n ---------------")
    for i in range(1,11):
        #x vai percorrer de 1 a 10
        resultado = i * numero
        #print(f" {numero}   x {i:>3}  = {resultado: >2}")
        print(" %2d   x  %3d  = %2d"%(numero,i,resultado))
tabuada(7)