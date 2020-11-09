#Eduardo Nunes

def quadrado(n):
    return n**2


def linhas(l):
    for x in range(1,l+1):
        #print(f"     {x}{quadrado(x): >13}")
        print(f"%6d %12d"%(x,quadrado(x)))

print ("Número     Quadrado")
linhas(5)