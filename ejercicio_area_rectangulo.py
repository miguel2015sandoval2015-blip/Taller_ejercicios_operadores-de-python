#************zona de funciones **********************
def definir_longitud():
    longitud = 30
    return longitud

def definir_ancho():
    ancho = 15
    return ancho

def calcular_area(longitud, ancho):
    area = (longitud * ancho)
    return area

def imprimir_datos(longitud, ancho):
    mensaje = "la longitud es: " + longitud
    mensaje = " el ancho es : " + ancho

def imprimir_resultado(resultado_area):
    print("el area del rectangulo es: " + str(resultado_area))

#********* zona de codigo principal***********************

ancho = definir_ancho()
longitud = definir_longitud()
area = calcular_area(ancho, longitud)    
resultado = imprimir_resultado(area)   