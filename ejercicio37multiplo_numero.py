#******** zona de funciones ***********
def ingresar_datos():
    num1 = int(input("digitar el primer numero: "))
    num2 = int(input("digitar el segundo"))
    return num1, num2

def procesar_datos(a,b):
    return a % b == 0

def mostrar_resultados(a, b, resultado):
    if resultado:
        print(a,"es multiplo de ", b)
    else:
        print(a,"NO es numero de ", b)
        
#******* zona de codigo principal *************
num1, num2 = ingresar_datos()
resultado = procesar_datos(num1, num2)
mostrar_resultados(num1, num2, resultado)            
    