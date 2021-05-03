import dictionary
import validador

def separador(palabra_recibida):
    x = palabra_recibida.split(" ")
    for i in x:
        if validador.validacion(i) != 100:
            print("Palabras denegadas")
            break
        else:
            print("Palabras aceptadas")
            continue



# def separador(palabra_recibida):
 #   x = palabra_recibida.split(" ")
  #  for i in dictionary.lista_comandos:
   #     if x[0] == i:
    #        dictionary.ayuda_comandos(x[0])
     #       break
      #  else:
       #     print("Comando no encontrado\nintente de nuevo\n")
        #    break