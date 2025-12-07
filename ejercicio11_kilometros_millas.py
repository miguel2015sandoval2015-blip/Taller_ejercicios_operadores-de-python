# *********** zona de funciones ************
def ingresar_kilometros():
    kilometros = float(input("digitar los kilometros a convertir: "))
    return kilometros

def capturar_datos(kilometros):
    milllas = (kilometros*0.621371)
    return milllas

def mostrar_datos(millas):
    print("las millas son: ", millas)
    
#*********** zona de codigo principal *****************
kilometros = ingresar_kilometros()
millas = capturar_datos(kilometros)
resultado = mostrar_datos(millas)    