#********* zona de funciones **********
def ingresar_datos():
    num1 = int(input("digite el primer numero entero: "))
    num2 = int(input("digite el segundo numero entero: "))
    return num1, num2

def procesar_datos(num1,num2):
    cociente = num1 // num2
    return cociente

def mostrar_resultados(cociente):
    print("el cociente de la division entera es: ",cociente)
    
#****** zona de codigo principal
num1 ,num2 = ingresar_datos()
cociente = procesar_datos(num1,num2)
resultado = mostrar_resultados(cociente)    
    