#************** zona de funciones ********************
def ingresar_grados():
    celcius = float(input("digitar los grados en celcius: "))
    return celcius


def capturar_datos(celcius):
    fahrenheit = (celcius*9/5)+32
    return fahrenheit


def mostrar_datos(fahrenheit):
    print("los grados fahrenheit son: ", fahrenheit)


#*********** zona de codigo principal *****************

celcius = ingresar_grados()
fahrenheit = capturar_datos(celcius)
celcius = mostrar_datos(fahrenheit)