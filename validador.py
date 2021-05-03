import os
import sys

lista_palabras = ["ayuda","listar","limpiar","concatenar","editar","directorio","salir"]

def validacion(palabraRecibida):
    if palabraRecibida == lista_palabras[0] or palabraRecibida == lista_palabras[1] or palabraRecibida == lista_palabras[2] or palabraRecibida == lista_palabras[3] or palabraRecibida == lista_palabras[4] or palabraRecibida == lista_palabras[5]:
        print(palabraRecibida)
        return 100
    elif palabraRecibida == lista_palabras[6]:
        print("\nSaliendo del interprete de comandos")
        sys.exit()
    else:
        print("\nError, comando no reconocido")
        return 0
     