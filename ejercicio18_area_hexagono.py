import math
#**************** zona de funciones ***************
def definir_longitud():
    longitud = float(input("digitar la longitud de un lado del hexagono: "))
    return longitud

def procesar_datos(longitud):
    area = (3 * math.sqrt(3) / (2))* (longitud ** 2)
    return area

def mostrar_resultados(area):
    print("el area del hexagono es: ", area)
    
def chao():
    print("el programa a finalizado")
    
#******* zona de codigo principal ***********
longitud = definir_longitud()
area = procesar_datos(longitud)
resultado = mostrar_resultados(area)
despedida = chao()        
