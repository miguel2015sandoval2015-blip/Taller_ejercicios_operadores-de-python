#****** zona de funciones ***********************
def ingresar_libras():
    libras = float(input("digitar las libras a convertir: "))
    return libras

def capturar_datos(libras):
    kilogramos = (libras*0.453592)
    return kilogramos

def mostrar_resultados(kilogramos):
    print("los kilogramos convertidos son: ", kilogramos)
    
def chao():
    print("el programa a finalizado")
    
#******* zona de codigo principal **************

libras = ingresar_libras()
kilogramos = capturar_datos(libras)
resultado = mostrar_resultados(kilogramos)
despedida = chao()

        