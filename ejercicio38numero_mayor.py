#***** zona de funciones ***********
def ingresar_datos():
    num1 = int(input("digitar el primer numero: "))
    num2 = int(input("digitar el segundo numero: "))
    return num1, num2

def procesar_datos(num1,num2):
    mayor = (num1 + num2 +abs(num1-num2))// 2 
    return mayor

def mostrar_resultados(mayor):
    print("el numero mayor es: ",mayor)
    
##********* zona de codigo principal *********
num1, num2 =ingresar_datos()
mayor = procesar_datos(num1,num2)
resultado = mostrar_resultados(mayor)    