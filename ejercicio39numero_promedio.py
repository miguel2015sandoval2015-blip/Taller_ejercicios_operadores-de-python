#***** zona de funciones *****
def ingresar_datos():
    num1 = float(input("digitar el primer numero: "))
    num2 = float(input("digitar el segundo numero: "))
    return num1, num2

def procesar_datos(num1,num2):
    promedio = (num1+num2) / 2
    return promedio

def mostrar_resultados(promedio):
    print("el promedio del numero es: ",promedio)

def chao():
    print("el programa a finalizado exitosamente")    
#****** zona de codigo principal ************
num1, num2 = ingresar_datos()
promedio = procesar_datos(num1,num2)
resultado = mostrar_resultados(promedio)
despedida = chao    