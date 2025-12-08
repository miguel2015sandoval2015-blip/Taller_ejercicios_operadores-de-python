#******** zona de funciones ***********
def ingresar_base():
    base = float(input("digite la base del triangulo: "))
    return base 

def ingresar_altura():
    altura = float(input("digitar la altura del triangulo: "))
    return altura

def procesar_datos(base,altura):
    area = (base * altura) / 2
    return area

def mostrar_resultados(area):
    print("el area del trianfulo es: ",area , ("centimetros cuadrados"))
    
#***** zona de codigo principal **************
base = ingresar_base()
altura = ingresar_altura()
area = procesar_datos(base,altura)
resultado = mostrar_resultados(area)    