#********* zona de funciones ***************
def capturar_numero():
    numero1 = int(input("digite el primer numero para la multiplicacion: "))
    return numero1

def definir_numero():
    numero2 = int(input("digite el segundo numero para la multiplicacion: "))
    return numero2

def procesar_datos(numero1,numero2):
    producto = numero1 * numero2
    return producto

def mostrar_resultados(producto):
    print("el resultado del producto es: ",producto)

def chao():
    print("el programa a finalizado")
    
#********* zona de codigo principal ************
numero1 = capturar_numero()
numero2 = definir_numero()
producto = procesar_datos(numero1,numero2)
resultado = mostrar_resultados(producto)   
despedida = chao()    