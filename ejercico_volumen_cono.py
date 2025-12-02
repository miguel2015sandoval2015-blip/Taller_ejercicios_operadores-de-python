#********** Zona de funciones ***************

def capturar_radio():
    radio = float(input("digitar el radio del cono: "))
    return radio

def capturar_altura():
    altura = float(input("digitar la altura del cono: "))
    return altura

def imprimir_datos(radio, altura):
    volumen = 1/3*3.1416*(radio**2)* altura
    return volumen

def mostrar_datos(volumen):
    print("el volumen del cono es: ", volumen)

#*********** zona de codigo princial *******************

radio = capturar_radio()
altura = capturar_altura()
volumen = imprimir_datos(radio, altura)
resultado = mostrar_datos(volumen)   