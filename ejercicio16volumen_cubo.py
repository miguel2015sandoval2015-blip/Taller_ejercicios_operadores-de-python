#*************** zona de funciones ************************

def definir_longitud():
    longitud = float(input("digitar el lado del cubo: "))
    return longitud

def procesar_datos(longitud):
    volumen = longitud*longitud*longitud
    return volumen

def mostrar_restultados(volumen):
    print("el volumen del cubo en metros cubicos es: ",volumen )
    
#********* zona de codigo principal ****************+
longitud = definir_longitud()
volumen = procesar_datos(longitud)
resultado = mostrar_restultados(volumen)    