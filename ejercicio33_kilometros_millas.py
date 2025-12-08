# *********** zona de funciones ************
def ingresar_kilometros():
    kilometros = float(input("digitar los kilometros a convertir en millas: "))
    return kilometros

def capturar_datos(kilometros):
    millas = (kilometros*0.621371)
    return millas

def mostrar_datos(millas):
    print("la distancia en millas son: ", millas,("millas"))
    
def chao():
    print("el programa a finalizado")    
    
#*********** zona de codigo principal *****************
kilometros = ingresar_kilometros()
millas = capturar_datos(kilometros)
resultado = mostrar_datos(millas)    
despedida = chao()