#******* zona de funciones *****************+
def capturar_horas():
    horas = float(input("digitar el numero de horas: "))
    return horas

def procesar_datos(horas):
    minutos = horas * 60
    return minutos

def mostrar_resultados(minutos):
    print("los minutos convertidos son: ",minutos)
    
#********* zona de codigo principal *******************+
horas = capturar_horas()
minutos = procesar_datos(horas)
resultado = mostrar_resultados(minutos)    
    