#clase que valida algunas palabras para su envio al ejecutador de comandos

import os
import sys
from subprocess import call

# lista de palabras reservadas
lista_palabras = ["ayuda","listar","directorio","limpiar","editar","concatenar","direcccionip","usocpu","comandos","listaservicios","servicio","arbol","lista","salir"]
limpia = ['clear']

def validacion(palabraRecibida):
    if palabraRecibida == lista_palabras[0] or palabraRecibida == lista_palabras[1] or palabraRecibida == lista_palabras[2] or palabraRecibida == lista_palabras[3] or palabraRecibida == lista_palabras[4] or palabraRecibida == lista_palabras[5] or palabraRecibida == lista_palabras[6] or palabraRecibida == lista_palabras[7] or palabraRecibida == lista_palabras[8] or palabraRecibida == lista_palabras[9] or palabraRecibida == lista_palabras[10] or palabraRecibida == lista_palabras[11] or palabraRecibida == lista_palabras[12]:
        #print(palabraRecibida)
        return 100
    elif palabraRecibida == lista_palabras[13]:
        call(limpia)
        print("\nSaliendo del interprete de comandos")
        sys.exit()
    else:
        if palabraRecibida == lista_palabras[0]:
            print("Menu de ayuda")
        else:
            print("\nError, comando no reconocido")
        return 0
     