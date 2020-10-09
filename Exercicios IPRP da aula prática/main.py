#Eduardo Nunes

def AreaTriangulo(comprimento, altura):
    AreaTotal = 0.5 * comprimento * altura
    return AreaTotal


comprimento = int(input("Comprimento: "))
altura = int(input("Altura: "))
Total = AreaTriangulo(comprimento, altura)

print("Area Total: "+ str(Total))