import os
import sys
import validador
import dictionary

listaComandos = ["listar","directorio","limpiar","editar","concatenar","direcccionip","usocpu"]


def buscadorComandos(listaRecibida):
    palabras = len(listaRecibida)
    print("Imprimiendo la lista")
    print(listaRecibida)
    for i in listaRecibida:
        if i == "ayuda":
            dictionary.ayuda_comandos(listaRecibida[1])
            break
        elif i == listaComandos[0]:
            os.system("ls")
            if palabras > 1:
                os.system("ls "+listaRecibida[1])
        elif i == listaComandos[1]:
            os.getcwd()
        elif i == listaComandos[2]:
            os.system("clear")
        elif i == listaComandos[3]:
            os.system("nano "+listaRecibida[1]) 
