#******** zona de funciones *************

def capturar_dolares():
    dolares = float(input("digitar la cantidad de dolares a convertir en euros"))
    return dolares

def ingresar_tasa():
    tasa = float(input("la tasa de cambio esta en: "))
    return tasa

def imprimir_datos(dolares, tasa):
    resultado = dolares* tasa
    return resultado

def mostrar_datos():
    print("los euros convertidos son: ", euros)

#******** zona principal de codigo **************

dolares = capturar_dolares()
tasa = ingresar_tasa()
euros= imprimir_datos(dolares, tasa)
resultado = mostrar_datos()
