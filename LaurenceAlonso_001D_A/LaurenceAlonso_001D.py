from os import system
system ("cls")

# FUNCIONES DE VALIDACION
def buscar_codigo(busqueda:str,inventario:dict):
    busqueda=busqueda.upper()
    for codigo in inventario:
        if busqueda==codigo:
            return True
    return False

def validar_codigo(codigo:str):
    codigo=codigo.upper()
    if codigo.strip():
        return True
    else:
        return False

def validar_titulo(titulo:str):
    titulo=titulo.upper()
    if titulo.strip():
        return True
    else:
        return False

def validar_plataforma(plataforma:str):
    plataforma=plataforma.upper()
    if plataforma.strip():
        return True
    else:
        return False

def validar_genero(genero:str):
    genero=genero.upper()
    if genero.strip():
        return True
    else:
        return False

def validar_clasificacion(clasificacion:str):
    clasificacion=clasificacion.upper()
    if not clasificacion.strip():
        return False
    if clasificacion=="E":
        return True
    elif clasificacion=="T":
        return True
    elif clasificacion=="M":
        return True
    else:
        return False

def validar_multiplayer(multiplayer:str):
    multiplayer=multiplayer.upper()
    if not multiplayer.strip():
        return False
    if multiplayer=="S":
        return "S"
    elif multiplayer=="N":
        return "N"
    else:
        return False

def validar_editor(editor:str):
    editor=editor.upper()
    if editor.strip():
        return True
    else:
        return False

def validar_precio(precio:str):
    try:
        precio=int(precio)
        if precio>0:
            return True
        return False
    except ValueError:
        return False

def validar_stock(precio:str):
    try:
        precio=int(precio)
        if precio>=0:
            return True
        return False
    except ValueError:
        return False

def validar_preciomin(p_min:str):
    try:
        p_min=int(p_min)
        if p_min>0:
            return True
        return False
    except ValueError:
        return False

def validar_preciomax(p_max:str):
    try:
        p_max=int(p_max)
        if p_max>0:
            return True
        return False
    except ValueError:
        return False

# FUNCIONES DEL PROGRAMA
def stock_plataforma(plataforma:str,juegos:dict,inventario:dict):
    total=0
    plataforma=plataforma.upper()

    for codigo in juegos:
        if plataforma == juegos[codigo][1]:
            total=total+inventario[codigo][1]
    print(f"EL STOCK ALMACENADO ES {total}")

def busqueda_precio(p_min:int,p_max:int,juegos:dict,inventario:dict):
    lista_coincidentes=[]

    for codigo in inventario:
        if inventario[codigo][0]>p_min and inventario[codigo][0]<p_max:
            if inventario[codigo][1]!=0:
                juego=[f"{juegos[codigo][0]}--{codigo}"]
                lista_coincidentes.append(juego)

    if lista_coincidentes:
        print(f"LA LISTA DE JUEGOS CON ESTE RANGO ES: {lista_coincidentes}")
    else:
        print("NO EXISTEN JUEGOS DENTRO DE ESE RANGO")


def actualizar_precio(busqueda:str,nuevo_precio:str,inventario:dict):
    try:
        nuevo_precio=int(nuevo_precio)
    except ValueError:
        return False
    inventario[busqueda][0]=nuevo_precio
    return True

def agregar_juego(codigo:str,titulo:str,plataforma:str,genero:str,clasificacion:str,multiplayer:str,editor:str,precio:int,stock:int,juegos:dict, inventario:dict):
    if codigo in juegos or codigo in inventario:
        return False
    juegos[codigo]=[titulo,plataforma,genero,clasificacion,multiplayer,editor]
    inventario[codigo]=[precio,stock]
    return True

def eliminar_juego(busqueda:str,juegos:dict,inventario:dict):
    del juegos[busqueda]
    del inventario[busqueda]
    return True


# FUNCIONES PRINCIPALES
def menu_principal():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por plataforma")
    print("2. Búsqueda de juegos por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")
    print("==============================")

def leer_opcion()->int:
    try:
        opcion=int(input("INGRESE UNA OPCIÓN: "))
        return opcion
    except ValueError:
        return 0

def continuar_programa():
    input("PRESIONE CUALQUIER TECLA PARA CONTINUAR... ")
    system("cls")


# PROGRAMA PRINCIPAL
def main():
    juegos= {}
    inventario={}

    while True:

        menu_principal()
        opcion=leer_opcion()

        if opcion == 1:
            plataforma=input("INGRESE LA PLATAFORMA DEL JUEGO A BUSCAR: ")
            stock_plataforma(plataforma,juegos,inventario)
            continuar_programa()

        elif opcion == 2:
            p_min=input("INGRESE EL LÍMITE INFERIOR DEL RANGO DE PRECIO: ")
            comprobacion=validar_preciomin(p_min)
            if not comprobacion:
                print("EL VALOR INGRESADO DEBE SER UN NÚMERO ENTERO MAYOR A CERO")
                continuar_programa()
                continue
            p_min=int(p_min)

            p_max=input("INGRESE EL LÍMITE SUPERIOR DEL RANGO DE PRECIO: ")
            comprobacion=validar_preciomax(p_max)
            if not comprobacion:
                print("EL VALOR INGRESADO DEBE SER UN NÚMERO ENTERO MAYOR A CERO")
                continuar_programa()
                continue
            p_max=int(p_max)

            if p_min > p_max:
                print("EL LÍMITE INFERIOR NO PUEDE SER MAYOR AL SUPERIOR.")
                continuar_programa()
                continue

            busqueda_precio(p_min,p_max,juegos,inventario)
            continuar_programa()

        elif opcion == 3:
            busqueda=input("INGRESE EL CÓDIGO DEL JUEGO: ")
            comprobacion=buscar_codigo(busqueda,inventario)
            if not comprobacion:
                print("NO SE HA PODIDO ENCONTRAR EL JUEGO.")
                continuar_programa()
                continue
            busqueda=busqueda.upper()
            nuevo_precio=input("INGRESE EL PRECIO NUEVO: ")

            resultado=actualizar_precio(busqueda,nuevo_precio,inventario)
            if resultado:
                print("EL PRECIO SE HA ACTUALIZADO CORRECTAMENTE.")
            else:
                print("NO SE HA PODIDO REALIZAR EL CAMBIO DE PRECIO.")
            continuar_programa()

        elif opcion == 4:
            codigo=input("INGRESE EL CÓDIGO DEL JUEGO: ")
            comprobacion=validar_codigo(codigo)
            if not comprobacion:
                print("EL CÓDIGO INGRESADO NO PUEDE ESTAR VACÍO.")
                continuar_programa()
                continue
            codigo=codigo.upper()

            titulo=input("INGRESE EL TÍTULO DEL JUEGO: ")
            comprobacion=validar_titulo(titulo)
            if not comprobacion:
                print("EL TÍTULO INGRESADO NO PUEDE ESTAR VACÍO.")
                continuar_programa()
                continue
            titulo=titulo.upper()

            plataforma=input("INGRESE LA PLATAFORMA DEL JUEGO: ")
            comprobacion=validar_plataforma(plataforma)
            if not comprobacion:
                print("LA PLATAFORMA INGRESADA NO PUEDE ESTAR VACÍA.")
                continuar_programa()
                continue
            plataforma=plataforma.upper()

            genero=input("INGRESE EL GÉNERO DE JUEGO: ")
            comprobacion=validar_genero(genero)
            if not comprobacion:
                print("EL GENERO INGRESADO NO PUEDE ESTAR VACÍO.")
                continuar_programa()
                continue
            genero=genero.upper()

            clasificacion=input("INGRESE LA CLASIFICACIÓN DEL JUEGO: ")
            comprobacion=validar_clasificacion(clasificacion)
            if not comprobacion:
                print("LA CLASIFICACIÓN DEBE ESTAR ENTRE 'E','T' Ó 'M'.")
                continuar_programa()
                continue
            clasificacion=clasificacion.upper()

            multiplayer=input("¿EL JUEGO ES MULTIJUGADOR? ")
            comprobacion=validar_multiplayer(multiplayer)
            if not comprobacion:
                print("EL VALOR INGRESADO DEBE SER 'S' Ó 'N'.")
                continuar_programa()
                continue
            multiplayer=multiplayer.upper()

            editor=input("INGRESE EL EDITOR DEL JUEGO: ")
            comprobacion=validar_editor(editor)
            if not comprobacion:
                print("EL EDITOR INGRESADO NO PUEDE ESTAR VACÍO.")
                continuar_programa()
                continue
            editor=editor.upper()

            precio=input("INGRESE EL PRECIO DEL JUEGO: ")
            comprobacion=validar_precio(precio)
            if not comprobacion:
                print("EL VALOR INGRESADO DEBE SER UN NÚMERO ENTERO MAYOR QUE CERO.")
                continuar_programa()
                continue
            precio=int(precio)

            stock=input("INGRESE EL STOCK DEL JUEGO: ")
            comprobacion=validar_stock(stock)
            if not comprobacion:
                print("EL VALOR INGRESADO DEBE SER UN NÚMERO ENTERO MAYOR O IGUAL A CERO.")
                continuar_programa()
                continue
            stock=int(stock)

            resultado=agregar_juego(codigo,titulo,plataforma,genero,clasificacion,multiplayer,editor,precio,stock,juegos,inventario)

            if resultado:
                print("SE HA AÑADIDO EL JUEGO CORRECTAMENTE.")
            else:
                print("ERROR: EL JUEGO YA EXISTE.")
            continuar_programa()

        elif opcion == 5:
            busqueda=input("INGRESE EL CÓDIGO DEL JUEGO QUE DESEA ELIMINAR: ")
            comprobacion=buscar_codigo(busqueda,inventario)
            if not comprobacion:
                print("NO SE HA PODIDO ENCONTRAR EL JUEGO.")
                continuar_programa()
                continue

            resultado=eliminar_juego(busqueda,juegos,inventario)
            if resultado:
                print("EL JUEGO SE HA ELIMINADO CORRECTAMENTE.")
            continuar_programa()

        elif opcion == 6:
            print("PROGRAMA FINALIZADO.")
            break

        else:
            print("ERROR: OPCIÓN INVÁLIDA.")
            continuar_programa()

main()