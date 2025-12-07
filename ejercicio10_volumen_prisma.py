#*********+ zona de funciones *****************
def definir_largobase():
    largoBase = float(input("digitar el largo del prima: "))
    return largoBase

def definir_anchobase():
    anchobase = float(input("digitar el ancho del prisma: "))
    return anchobase

def definir_altura():
    altura = float(input("digitar la altura del prisma: "))
    return altura

def prcesar_datos(largoBase , anchobase , altura):
    volumen = largoBase * anchobase * altura
    return volumen

def imprimir_datos(volumen):
    print("el volumen del prima en metros cubicos es: ", volumen)
    
def chao():
    print("el programa a finalizado con exito")
    
    
#**************** zona de codigo principal *****************
largoBase = definir_largobase()
ancho_base = definir_anchobase()
altura = definir_altura()
volumen = prcesar_datos(largoBase,ancho_base,altura)
resultado = imprimir_datos(volumen)
despidida = chao()    
   