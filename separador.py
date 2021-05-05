# clase encargada de separar la cadena del usuario, para enviar cada argumento

import dictionary
import validador
import comandos

#metodo para separar la cadena recibida del usuario
def separador(palabra_recibida):
    #se genera una lista vacia para enviar los comandos al seleccionador de comandos
    lista = []
    x = palabra_recibida.split(" ")
    for i in x:
        #se verifica si la palabra es reservada
        if validador.validacion(i) != 100:
            print("\nPalabras denegadas, revise la sintaxis")
            lista.append(i)
            break
        else:
            #print("\nPalabras aceptadas")
            lista.append(i)
            continue
        #se envian los comandos aceptados para su ejecucion
    comandos.buscadorComandos(lista)


# def separador(palabra_recibida):
 #   x = palabra_recibida.split(" ")
  #  for i in dictionary.lista_comandos:
   #     if x[0] == i:
    #        dictionary.ayuda_comandos(x[0])
     #       break
      #  else:
       #     print("Comando no encontrado\nintente de nuevo\n")
        #    break