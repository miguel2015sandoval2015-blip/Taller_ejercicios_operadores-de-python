#********** zona de funciones ******************
def definir_pi():
    pi = 3.1416
    return pi

def definir_radio():
    print("digite el radio del circulo")
    radio=int(input())
    return radio

def calcular_volumen(pi, radio):
    volumen = (radio**3 * pi)* 3/4
    return volumen

def imprimir_datos(pi, radio):
    mensaje = "el numero pi es: " + pi
    mensaje = "el radio es: " + radio

def imprimir_resultado(resultado_volumen):
    print("el volumen de la esfera es: " + str(resultado_volumen))

#*************** zona principal del codigo ************

pi = definir_pi()
radio = definir_radio()
volumen = calcular_volumen(pi,radio)
resultado = imprimir_resultado(volumen)    
