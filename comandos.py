# clase que contiene la definicion de los comandos

import os
import sys
import validador
import dictionary
from subprocess import call

# listas para ejecucion de comandos 
listaComandos = ["listar","directorio","limpiar","editar","concatenar","direccionip","usocpu","listaservicios","servicio"]
serviciosArbol = ['systemctl','status']
serviciosLista = ['systemctl','-a']
servicioExplicito = "systemctl status "

#funcion que ejecuta los comandos finales
def buscadorComandos(listaRecibida):
    palabras = len(listaRecibida)
    #print("Imprimiendo la lista")
    #print(listaRecibida)
    for i in listaRecibida:
        if palabras > 2:
            print("\nDemasiados argumentos, o comando no reconocido")
        else:
            if i == "ayuda":
                if palabras > 1:
                    dictionary.ayuda_comandos(listaRecibida[1])
                    break
                else:
                    dictionary.ayuda_comandos(listaRecibida[0])
                    break
            elif i == listaComandos[0]:
                if palabras > 1:
                    os.system("ls "+listaRecibida[1])
                else:
                    os.system("ls")
            elif i == listaComandos[1]:
                os.system("pwd")
                print("\r<--- Directorio actual de trabajo")
            elif i == listaComandos[2]:
                os.system("clear")
            elif i == listaComandos[3]:
                if palabras > 1:
                    os.system("nano "+listaRecibida[1])
                else:
                    os.system("nano")
            elif i == listaComandos[4]:
                os.system("cat "+listaRecibida[1])
            elif i == listaComandos[5]:
                os.system("ip addr")
            elif i == listaComandos[6]:
                os.system("top")
            elif i == listaComandos[7]:
                if palabras > 1:
                    if listaRecibida[1] == "arbol":
                        call(serviciosArbol)
                    elif listaRecibida[1] == "lista":
                        call(serviciosLista)
                else:
                    print("\nSe necesita al menos un tipo de vista especifica, arbol o lista")
            elif i == listaComandos[8]:
                if palabras > 1:
                    os.system(servicioExplicito + listaRecibida[1])
                else:
                    print("\nSe necesita al menos un servicio para verificar su estatus\nUso: servicio 'nombre_del_servicio'")