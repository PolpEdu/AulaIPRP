#Eduardo Nunes

def cadeia(string):
    lenght = len(string)
    divisions= round(lenght / 3)

    for x in range(divisions):
        print(string[x*3:3*(x+1)])

x =str(input("Diz uma palavra: "))
cadeia(x)