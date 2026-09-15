import funcion3

def main():
    opcion = 0

    while opcion != 5:
        print("----------- MENU -----------")
        print("1. Cargar servicios")
        print("2. Mostrar servicios que esten entre i1 e i")
        print("3. Mostrar servicios activos")
        print("4. Buscar servicio por Nombre")
        print("5. Salir")

        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            funcion3.cargar()

        if opcion == 2:
            funcion3.importes(funcion3.objetos)

        if opcion == 3:
            funcion3.servicios(funcion3.objetos)

if __name__ == "__main__":
    main()
