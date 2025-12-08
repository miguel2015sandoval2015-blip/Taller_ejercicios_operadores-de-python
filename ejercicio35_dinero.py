#****** zona de funciones *******
def definir_cantidad():
    dinero = float(input("digite la cantidad de dinero que tiene en la cuenta: "))
    return dinero

def procesar_datos(dinero):
    interes = dinero * 0.05
    return interes

def mostrar_datos(interes):
    print("el interes es:$",interes)
    
#***** zona de codigo principal *************
dinero = definir_cantidad()
interes = procesar_datos(dinero)
resultado = mostrar_datos(interes)    