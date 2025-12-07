#**************zona de funciones **********************
def  definir_longitud():
    longitud = float(input("digitar la longitud del cuadrado en cm: "))
    return longitud

def procesar_datos(longitud):
    area = longitud * longitud
    return area

def imprimir_datos(area):
    print("el area del caudro es cm2: ", area)
    
def chao():
    print("el programa a finalizado")
    
# ******** zona de codigo principal ****************
longitud = definir_longitud()
area = procesar_datos(longitud)
resultado = imprimir_datos(area)
despedida = chao()        
    