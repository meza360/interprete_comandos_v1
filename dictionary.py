lista_comandos = {
        "ayuda": "\nAyuda\n Muestra esta ventana de informacion\nPara mostrar todos los comandos disponibles, puede ingresar 'ayuda comandos'",
        "listar": "\nLista los archivos en el directorio actual\n Uso: listar ó listar ruta/",
        "directorio": "\nMuestra la ruta sobre la cual se esta trabajando actualmente\n Uso: directorio",
        "limpiar": "\nLimpia la pantalla actual en la terminal\n Uso: limpiar",
        "editar": "\nAbre el editor de texto con el archivo seleccionado\n Uso: editar archivo.txt",
        "concatenar": "\nMuestra el contenido de el archivo seleccionado\n Uso: concatenar archivo.txt",
        "direccionip": "\nMuestra las direcciones IP en las interfaces de red\n Uso: direccionip",
        "usocpu": "\nMuestra el menu del uso del CPU con informacion detallada\n Uso: usocpu",
        "listaservicios": "\nMuestra una lista de los servicios que corren en la maquina\n Uso: listaservicios"

    }

ayuda = "\nAyuda\n Muestra esta ventana de informacion\nPara mostrar todos los comandos disponibles, puede ingresar 'ayuda comandos'"
listar = "\nlistar \nLista los archivos en el directorio actual\n Uso: listar ó listar ruta/"
directorio = "\ndirectorio \nMuestra la ruta sobre la cual se esta trabajando actualmente\n Uso: directorio"
limpiar = "\nlimpiar \nLimpia la pantalla actual en la terminal\n Uso: limpiar"
editar = "\neditar \nAbre el editor de texto con el archivo seleccionado\n Uso: editar archivo.txt"
concatenar = "\nconcatenar \nMuestra el contenido de el archivo seleccionado\n Uso: concatenar archivo.txt"
direccionip = "\ndireccionip \nMuestra las direcciones IP en las interfaces de red\n Uso: direccionip"
usocpu = "\nusocpu \nMuestra el menu del uso del CPU con informacion detallada\n Uso: usocpu"
listaservicios = "\nlistaservicios \nMuestra una lista de los servicios que corren en la maquina\n Uso: listaservicios"


listaCompleta = f"{ayuda} \n {listar} \n {directorio} \n {limpiar} \n{editar} \n{concatenar} \n{direccionip} \n{usocpu} \n{listaservicios}"

def ayuda_comandos(keyword):
    if keyword != "comandos":
        print(lista_comandos[keyword])
    else:
        print(listaCompleta)
