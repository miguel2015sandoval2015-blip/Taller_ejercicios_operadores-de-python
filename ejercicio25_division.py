#******** zona de fucniones ******************
def capturar_numero():
    numero = float(input("digitar el numero a dividir"))
    return numero

def capturar_divisor():
    divisor = float(input("digite el divisor: "))
    return divisor

def procesar_datos(numero,divisor):
    cociente = numero/divisor
    return cociente

def mostrar_resultado(cociente):
    print("el resultado de la divion es: ", cociente)
    
def chao_con_adios():
    print("el programa a finalizado")
    
#***** zona de codigo principal ***************
numero = capturar_numero()
divisor = capturar_divisor()
cociente = procesar_datos(numero,divisor)
resultado = mostrar_resultado(cociente)
despedida = chao_con_adios()        

