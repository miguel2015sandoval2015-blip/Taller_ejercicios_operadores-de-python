#************** zona de funciones *****************

def definir_Basemayor():
    Basemayor = float(input("digitar la Base Mayor del trapecio"))
    return Basemayor

def definir_basemenor():
    basemenor = float(input("digitar la base menor del trapecio"))
    return basemenor

def definir_altura():
    altura = float(input("digitar la altura del trapecio"))
    return altura

def procesar_datos(Basemayor,basemenor,altura):
    area = (Basemayor + basemenor) * altura / 2
    return area 

def mostrar_resultados(area):
    print("el area del trapecio es: ", area)
    
#*************** Zona de codigo principal *********************
Basemayor = definir_Basemayor()
basemenor = definir_basemenor()
altura = definir_altura()
area = procesar_datos(Basemayor,basemenor,altura)
resultado = mostrar_resultados(area)   
    