#******* zona de funciones *************
def ingresar_litros():
    litros = float(input("digitar los litros a convertir: "))
    return litros

def capturar_datos(litros):
    galones = litros*0.264172
    return galones

def mostrar_resultados(galones):
    print("los galones covertidos son: ",galones)

#********** zona de codigo principal***********+
litros = ingresar_litros()
galones = capturar_datos(litros)
resultado = mostrar_resultados(galones)
    