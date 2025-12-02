#******* zona de funciones *************************

def capturar_radio():
    radio = float(input("digitar el radio del cilindro: "))
    return radio

def capturar_altura():
    altura = float(input("digite la altura del cilindro: "))
    return altura

def imprimir_datos(radio, altura):
    volumen = 3.1416*(radio*2) * altura
    return volumen

def imprimir_resultados(volumen):
    print("el volumen en el cilindro es: ", volumen)



#***************** Zona de codigo principal **************************

radio = capturar_radio()
altura = capturar_altura()
volumen = imprimir_datos(radio, altura)
resultado = imprimir_resultados(volumen)