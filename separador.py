import dictionary

def separador(palabra_recibida):
    x = palabra_recibida.split(" ")
    for i in dictionary.lista_comandos:
        if x[0] == i:
            dictionary.ayuda_comandos(x[0])
            break
        else:
            print("Comando no encontrado\nintente de nuevo\n")
            break