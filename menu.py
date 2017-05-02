def mostrar_menu_de_bienvenida():
        print("Bienvenido a Light out")
def mostrar_modo_de_juego():
    print("Elija modo de juego")
    print("1 - Predeterminado")
    print("2 - Aleatorio")
    print("3 - Salir")
    modoElegido=input()

    if (modoElegido == "1"):
        print("Ha elegido juego en modo predeterminado")
    elif (modoElegido == "2"):
        print("Ha elegido juego en modo aleatorio")
    elif (modoElegido== "3" ):
        print ("Ha elegido salir")