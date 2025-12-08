#********* zona de funciones *********************
def capturar_numero():
    numero =int(input("digite el primer numero: "))
    return numero

def capturar_otronumero():
    numero = int(input("digite el segundo numero: "))
    return numero

def procesar_datos(num1,num2):
    resta = num1 - num2
    return resta

def mostrar_resultados(resta):
    print("las resta de los numeros es: ", resta)

#******* zona de codigo principal ****************
num1 = capturar_numero()
num2 = capturar_otronumero()
resta = procesar_datos(num1, num2)
resultado = mostrar_resultados(resta)
    