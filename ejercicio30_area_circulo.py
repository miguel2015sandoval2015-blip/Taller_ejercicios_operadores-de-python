#*******+ zona de funciones *****************+
def ingresar_radio():
    radio = float(input("digitar el radio del circulo: "))
    return radio

def procesar_datos(radio):
    circuferencia = 2 * 3.1416 * radio
    return circuferencia

def mostrar_resultados(circunferencia):
    print("la circunferencia del circulo es: ", circunferencia)
    
def chao():
    print("el programa a finalizado")

#******** zona de codigo principal *************
radio = ingresar_radio()
circunferencia = procesar_datos(radio)
resultado = mostrar_resultados(circunferencia)
despedida = chao        