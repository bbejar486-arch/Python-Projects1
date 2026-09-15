import funcion2


def menu():
    opcion = 0

    while opcion != 5:

        print("----------- MENU -----------")
        print("1. Cargar tickets")
        print("2. Mostrar tickets con asiento mayor a un numero")
        print("3. Mostrar importes acumulados por pais")
        print("4. Buscar ticket por identificacion")
        print("5. Salir")

        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            funcion2.cargar()

        elif opcion == 2:
            funcion2.mayor_asiento(funcion2.tickets)

        elif opcion == 3:
            funcion2.importes(funcion2.tickets)

        elif opcion == 4:
            funcion2.busqueda(funcion2.tickets)

        elif opcion == 5:
            print("Programa finalizado")

        else:
            print("Opcion incorrecta")


if __name__ == "__main__":
    menu()
