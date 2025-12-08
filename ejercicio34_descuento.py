#*** zona de funciones *******************
def ingresar_precio():
    precio = float(input("digitar el precio del producto: "))
    return precio

def procesar_datos(precio):
    descuento = precio *0.10
    precio_final = precio - descuento
    return descuento , precio_final

def mostrar_resultados(descuento, precio_final):
    print("el descuento aplicado es: ", descuento)
    print("el precio final con el descuento es: ", precio_final)
    
#******* zona de codigo principal **********
precio = ingresar_precio()
descuento, precio_final = procesar_datos(precio)
mostrar_resultados(descuento, precio_final)    