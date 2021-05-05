# esta es la clase principal
# se puede invocar con el interprete de python, desde linux, ingresando
# python main.py

import dictionary
import separador

#bucle infinito para la constante peticion de el input del usuario
while True:
    palabra = input("Ingrese un comando ó ingrese 'Ayuda' para mostrar una guia\n")
    separador.separador(palabra)
