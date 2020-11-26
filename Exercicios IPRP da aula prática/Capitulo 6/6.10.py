#Eduardo Nunes
autor = {"php":"Rasmus Lerdorf","perl":"Larry Wall","tcl":"John Ousterhout",
"awk":"Brian Kernighan","java":"James Gosling","parrot":"Simon Cozens",
"python":"GuidovanRossum","xpto":"zxcv"}

def modificar(dicionario):
    #a
    dicionario["Javascript"] = "Brendan Eich"

    #b
    dicionario["python"]="Guido van Rossum"

    #c
    dicionario.pop("xpto")

    #d
    print(len(dicionario))

    #e
    if "c++" in dicionario.keys():
        print("c++ está no dicionario")
    else:
        print("Não está")
    print(dicionario)

modificar(autor)
#https://codeshare.io/2B1gDb