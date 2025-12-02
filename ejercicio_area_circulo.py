#************** zona de funciones ********************

def capturar_radio():
    radio = float(input("digitar el radio del circulo "))
    return radio

def definir_pi():
    pi = 3.1416
    return pi

def imprimir_datos(radio, pi):
    area = 3.1416*(radio*2)
    return area

def mostrar_datos(area):
    print("area del circulo es: ", area)

 #***************** zona de funciones ****************

radio = capturar_radio()
pi = definir_pi()
area = imprimir_datos(radio, pi)
resultado = mostrar_datos(area)