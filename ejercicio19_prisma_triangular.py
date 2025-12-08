#********** zona de funciones ********************
def definir_longitudBase():
    longitudbase = float(input("digitar la longitud de la base del prisma triangular: "))
    return longitudbase

def definir_altura():
    altura = float(input("digitar la altura del prisma: "))
    return altura

def definir_ancho():
    ancho = float(input("digitar el ancho del prisma: "))
    return ancho

def procesar_datos (longitudbase,altura,ancho):
    volumen =(longitudbase*altura)/2*(ancho)
    return volumen

def mostrar_resultados(volumen):
    print("el volumen de prisma triangular es: ", volumen,("centimetros cubicos"))
    
#********* zona de codigo principal ***************

longitudbase = definir_longitudBase()
altura = definir_altura()
ancho = definir_ancho()
volumen = procesar_datos(longitudbase,altura,ancho)
resultado = mostrar_resultados(volumen)   