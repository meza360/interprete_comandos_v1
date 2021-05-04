import os
import sys
import validador
import dictionary

listaComandos = ["listar","limpiar","concatenar","editar"]


def buscadorComandos(listaRecibida):
    print("Imprimiendo la lista")
    print(listaRecibida)
    for i in listaRecibida:
        if i == "ayuda":
            dictionary.ayuda_comandos(listaRecibida[1])
            break
        elif i == listaComandos[0]:
            os.getcwd()
        elif i == listaComandos[1]:
            os.system("dir")
