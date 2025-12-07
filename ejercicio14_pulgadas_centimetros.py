# ******************** zona de funciones ******************************
def ingresar_pulgadas():
    pulgadas = float(input("digitar la pulgadas a convertir: "))
    return pulgadas

def capturar_datos(pulgadas):
    centimentros = (pulgadas*2.54)
    return centimentros

def mostrar_resultados(centimetros):
    print("los centimetros son: ", centimetros)
    
#***** zona de codigo principal*************
pulgadas = ingresar_pulgadas()
centimetros = capturar_datos(pulgadas)
resultado = mostrar_resultados(centimetros)    