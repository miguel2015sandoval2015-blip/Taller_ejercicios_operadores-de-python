#***************+ zona de funciones *********************
def capturar_numero():
    numero = int(input("digite un numero para la sumatoria: "))
    return numero

def capturar_numeros():
    numeros = int(input("digite el otro numero para la sumatoria total: "))
    return numeros

def procesar_datos(numero,numeros):
    sumatoria = numero + numeros
    return sumatoria

def mostrar_ressultados(sumatoria):
    print("la sumatoria de los 2 numeros es: ", sumatoria)
    
#*********** zona de codigo principal *********************
numero = capturar_numero()
numeros = capturar_numeros()
sumatoria = procesar_datos(numero,numeros) 
resultados = mostrar_ressultados(sumatoria)   