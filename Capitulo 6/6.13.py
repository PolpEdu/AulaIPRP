#Eduardo Nunes
def dicionario(string):
    newstring = ""
    dias_semana = {
        1:'Domingo',
        2:'Segunda - Feira',
        3:'Terça - feira',
        4:'Quarta - feira',
        5:'Quinta - feira',
        6:'Sexta - feira',
        7:'Sábado'}
    meses_ano ={
        1:'Janeiro',
        2:'Fevereiro',
        3:'Março',
        4:'Abril',
        5:'Maio',
        6:'Junho',
        7:'Julho',
        8:'Agosto',
        9:'Setembro',
        10:'Outubro',
        11:'Novembro',
        12:'Dezembro'
    }
    numbers = string.split("/")

    newstring += dias_semana.get(int(numbers[0])) + ", "
    newstring +=numbers[1] + " de "
    newstring +=meses_ano.get(int(numbers[2])) + " de "
    newstring+= numbers[3]
    print(f"Fornecido: {string}")
    return newstring
print(dicionario("4/5/6/2006"))
#https://codeshare.io/5zrD67
