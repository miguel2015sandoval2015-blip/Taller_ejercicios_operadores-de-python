#******************* zona de funciones ********************

def definir_longitudbase():
    longuitud = float(input("digitar la longitud de la base de la piramide: "))
    return longuitud

def definir_ancho():
    ancho = float(input("digitar el ancho de la base de la piramide: "))
    return ancho

def definir_altura():
    altura = float(input("digitar la altura de la piramide: "))
    return altura

def procesar_datos(longuitud,ancho,altura):
    volumen = (longuitud * ancho * altura) / 3
    return volumen
    
def mostrar_resultado(volumen):
    print("el volumen de la piramide en metros cubicos es: ", volumen)
    
def chao():
    print("el programa a finalizado exitosamente")
    
#***** zona de codigo principal ***********************
longuitud = definir_longitudbase()
ancho = definir_ancho()
altura = definir_altura()
volumen = procesar_datos(longuitud,ancho,altura)
resultado = mostrar_resultado(volumen)
despedida = chao()            