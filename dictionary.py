lista_comandos = {
        "ayuda": "Ayuda\n Muestra esta ventana de informacion",
        "listar": "Lista los archivos en el directorio actual",
    }
lista_palabras = {"ayuda","listar","limpiar","concatenar","editar"}

def ayuda_comandos(keyword):
    print(lista_comandos[keyword])
    
