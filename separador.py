import dictionary
import validador
import comandos


def separador(palabra_recibida):
    lista = []
    x = palabra_recibida.split(" ")
    for i in x:
        if validador.validacion(i) != 100:
            print("\nPalabras denegadas, revise la sintaxis")
            lista.append(i)
            break
        else:
            #print("\nPalabras aceptadas")
            lista.append(i)
            continue
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