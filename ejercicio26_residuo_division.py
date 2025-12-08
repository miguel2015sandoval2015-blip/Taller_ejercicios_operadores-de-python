#********* zona de funciones *************
def capturar_dividendo():
    dividendo = int(input("digite el numero del dividendo: "))
    return dividendo

def capturar_divisor():
    divisor = int(input("digite el numero divisor: "))
    return divisor

def procesar_datos(dividendo,divisor):
    residuo = dividendo % divisor
    return residuo

def mostrar_resultados(residuo):
    print("el residuo de la division es:", residuo)
    
#************** zona de codigo principal *************
dividendo = capturar_dividendo()
divisor = capturar_divisor()
residuo = procesar_datos(dividendo,divisor)
resultado = mostrar_resultados(residuo)    