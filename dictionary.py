# esta clase solamente contiene el diccionario de comandos para el interprete

# diccionario de comandos
lista_comandos = {
        "ayuda": "\nAyuda\n Muestra esta ventana de informacion\nPara mostrar todos los comandos disponibles, puede ingresar 'ayuda comandos'",
        "listar": "\nLista los archivos en el directorio actual\n Uso: listar ó listar ruta/",
        "directorio": "\nMuestra la ruta sobre la cual se esta trabajando actualmente\n Uso: directorio",
        "limpiar": "\nLimpia la pantalla actual en la terminal\n Uso: limpiar",
        "editar": "\nAbre el editor de texto con el archivo seleccionado\n Uso: editar archivo.txt",
        "concatenar": "\nMuestra el contenido de el archivo seleccionado\n Uso: concatenar archivo.txt",
        "direccionip": "\nMuestra las direcciones IP en las interfaces de red\n Uso: direccionip",
        "usocpu": "\nMuestra el menu del uso del CPU con informacion detallada\n Uso: usocpu",
        "listaservicios": "\nMuestra una lista de los servicios que corren en la maquina\n Uso: listaservicios",
        "servicio": "\nservicio \nMuestra la informacion sobre un servicio en especifico, para lo cual, debe saber el nombre del proceso, puede encontrarlo con el comando 'listaservicios' \nUso: servicio 'nombre_del_servicio'"

    }

# variables usadas en f-String
# de esta manera, cada definicion se puede cambiar a conveniencia
ayuda = "\nAyuda\n Muestra esta ventana de informacion\nPara mostrar todos los comandos disponibles, puede ingresar 'ayuda comandos'"
listar = "\nlistar \nLista los archivos en el directorio actual\n Uso: listar ó listar ruta/"
directorio = "\ndirectorio \nMuestra la ruta sobre la cual se esta trabajando actualmente\n Uso: directorio"
limpiar = "\nlimpiar \nLimpia la pantalla actual en la terminal\n Uso: limpiar"
editar = "\neditar \nAbre el editor de texto con el archivo seleccionado\n Uso: editar archivo.txt"
concatenar = "\nconcatenar \nMuestra el contenido de el archivo seleccionado\n Uso: concatenar archivo.txt"
direccionip = "\ndireccionip \nMuestra las direcciones IP en las interfaces de red\n Uso: direccionip"
usocpu = "\nusocpu \nMuestra el menu del uso del CPU con informacion detallada\n Uso: usocpu"
listaservicios = "\nlistaservicios \nMuestra una lista de los servicios que corren en la maquina, en forma de arbol, o en forma de lista\n Uso: listaservicios arbol ó listaservicios lista"
servicio = "\nservicio \nMuestra la informacion sobre un servicio en especifico, para lo cual, debe saber el nombre del proceso, puede encontrarlo con el comando 'listaservicios' \nUso: servicio 'nombre_del_servicio'"

# se imprimen todas las variables anteriores
listaCompleta = f"{ayuda} \n {listar} \n {directorio} \n {limpiar} \n{editar} \n{concatenar} \n{direccionip} \n{usocpu} \n{listaservicios} \n{servicio}"

#metodo para mostrar la ayuda del comando solicitado por el separador
def ayuda_comandos(keyword):
    if keyword != "comandos":
        print(lista_comandos[keyword])
    else:
        print(listaCompleta)
