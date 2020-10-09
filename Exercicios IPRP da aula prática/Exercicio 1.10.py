#Eduardo Nunes
def ConverterTemp(Tc):
    Tf = 9/5 *  Tc + 32
    return Tf

TC = int(input("Escolha a temperatura em Celsius: "))

print("A temperatura em Fahrenheit é", ConverterTemp(TC) )

