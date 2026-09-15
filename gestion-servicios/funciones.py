from clases import Objetos
 
objetos = []

def cargar ():
    n = int(input("Ingrese cantidad de servicios vendidos: "))

    for i in range(n):
        print("----------------")

        numeros = "0123456789"
        valido = True
    

        codigo = str(input("Ingrese codigo identificatorio: "))

        if codigo == "" or codigo == " ":
            valido = False
        else:
            for i in codigo:
                if i not in numeros:
                    valido = False

        while valido == False:
            print("Codigo Incorrecto")
            codigo = input("Ingrese codigo identificatorio: ")

            valido = True

            if codigo == "" or codigo == " ":
                valido = False
            else:
                for i in codigo:
                    if i not in numeros:
                        valido = False

        codigo = int(codigo)

        nombre = input("Ingrese nombre del cliente: ")

        while nombre == "":
            print("Nombre incorrecto")
            nombre = input("Ingrese un nombre: ")


        servicio = int(input("Ingrese el tipo de servicio entre 1 y 10: "))

        while servicio < 1 or servicio > 10:
            print("Servicio incorrecto")
            servicio = int(input("Ingrese el servicio correcto: "))

        importe = str(input("Ingrese importe del servicio: "))

        val = True

        while importe <= "0" and val == False:
            for i in importe:
                if i not in numeros:
                    val = False
            print("importe incorrecto")
            importe = input("Ingrese un importe correcto: ")

        importe = int(importe)

        obj = Objetos(codigo, nombre, servicio, importe)
        objetos.append(obj)

    print("Datos cargados")

def importes(objetos):
    i1 = int(input("Ingrese i1: "))
    i2 = int(input("Ingrese i2: "))
    valores = []
    contador = 0

    for c in objetos:
        if c.importe >= i1 and c.importe <= i2:
            valores.append(c)

    for i in range(len(objetos)):
        for j in range(i+1 ,len(objetos)):
            if objetos[i].codigo > objetos[j].codigo:
                objetos[i], objetos[j] = objetos[j] , objetos[i]

    for i in range(len(valores)):
        print(valores[i])
        contador += 1

    print("------------------")
    print("Cantidad de servicios", contador)

def servicios (objetos):
    acumulador = [0] * 10

    for i in range(len(objetos)):
        acumulador[objetos[i].servicio - 1] += 1

    for i in range(len(acumulador)):
        if acumulador[i] != 0:
            print("Servicios activos: ",i+1, acumulador[i])


def busqueda(objetos):
    nom = input("Ingrese nombre para la busqueda: ")
    bandera = False
    encontrado = []

    for i in objetos:
        if bandera == False:
            if i.nombre == nom:
                bandera = True
                i.importe += 2000
                encontrado.append(i)
        else:
            break

    if bandera == False:
        print("Nombre no encontrado")
    else:
        print(encontrado)




