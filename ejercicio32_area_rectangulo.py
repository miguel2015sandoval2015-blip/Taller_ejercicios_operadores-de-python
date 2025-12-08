#**** zona de funciones ****************
def ingresar_longitud():
    longitud = float(input("digitar la longitud del rectangulo: "))
    return longitud

def ingresar_ancho():
    ancho = float(input("digitar el ancho del rectangulo: "))
    return ancho

def procesar_datos(longitud,ancho):
    area = longitud * ancho
    return area

def mostrar_resultados(area):
    print("el area del rectangulo es: ",area,("cm2"))
    
#******** zona de codigo principal ¨*********
longitud = ingresar_longitud()
ancho = ingresar_ancho()
area = procesar_datos(longitud,ancho)
resultado = mostrar_resultados(area)
    