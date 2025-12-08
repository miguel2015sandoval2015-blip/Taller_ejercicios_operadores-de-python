#***************++ zona de funciones **********+
def capturar_numero():
    numero = int(input("digite el numero para calcular la raiz cuadrada: "))
    return numero

def procesar_datos(numero):
    raiz = numero * 0.5
    return raiz

def mostrar_resultados(raiz):
    print("la raiz de numero es: ", raiz)
    
#*****+ zona de codigo principal ***************
numero = capturar_numero()
raiz = procesar_datos(numero)
resultado = mostrar_resultados(raiz)    
    
    