#******* zona de funciones ************
def capturar_numero():
    numero = int(input("digite numero que quiere calcular al cuadrado: "))
    return numero

def procesar_datos(numero):
    cuadrado = numero*numero
    return cuadrado

def mostrar_resultados(cuadrado):
    print("el numero al cuadrado es: ", cuadrado)
    
#************ zona de codigo principal ***********
numero = capturar_numero()
cuadrado = procesar_datos(numero)
resultados = mostrar_resultados(cuadrado)
