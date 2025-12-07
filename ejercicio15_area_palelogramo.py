#****** zona de funciones ************

def definir_longitud():
    longitud = float(input("digitar la longitud de la base del paralelogramo: "))
    return longitud

def definir_altura():
    altura = float(input("digitar la altura del paralelogramo: "))
    return altura

def procesar_datos(longitud,altura):
    area = longitud * altura
    return area

def mostrar_datos(area):
    print("el area del paralelogramo en metros cuadrados es: ", area)

def chao():
    print("el programa a finalizado")    
#******************* zona de codigo principal***************
longitud = definir_longitud()
altura = definir_altura()
area = procesar_datos(longitud,altura)
resultado = mostrar_datos(area)    
despedida = chao()