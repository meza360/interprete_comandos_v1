def ayuda_comandos(keyword):
    lista_comandos = {
        "Ayuda": "Ayuda\n Muestra esta ventana de informacion",
        "Listar": "Lista los archivos en el directorio actual",
    }
    print(lista_comandos[keyword])