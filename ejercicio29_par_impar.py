#****** zona de funciones ***********
def capturar_numero():
    numero = int(input("digite un numero: "))
    return numero

def procesar_datos(numero):
    if numero % 2== 0:
        return "par"
    else:
        return "impar"
    
def mostrar_resultado(resultado):
    print("el numero es: ", resultado)
    
#*********** zona de codigo principal ***********
numero = capturar_numero()
resultado = procesar_datos(numero)
mostrar_resultado(resultado)        