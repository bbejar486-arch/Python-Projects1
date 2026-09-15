class Ticket:
    def __init__(self, codigo, identificacion, pais, asiento, importe):
        self.codigo = codigo
        self.identificacion = identificacion
        self.pais = pais
        self.asiento = asiento
        self.importe = importe

    def __str__(self):
        return (
            "Vuelo: " + self.codigo +
            " - ID: " + self.identificacion +
            " - Pais: " + str(self.pais) +
            " - Asiento: " + str(self.asiento) +
            " - Importe: " + str(self.importe)
        )


tickets = []


def cargar():
    n = int(input("Ingrese cantidad de tickets vendidos: "))

    for i in range(n):

        print("Datos del ticket")
        print("------------------------")

        codigo = input("Ingrese codigo de vuelo: ")

        while codigo.strip() == "":
            print("Codigo incorrecto")
            codigo = input("Ingrese codigo de vuelo: ")

        identificacion = input("Ingrese numero de identificacion: ")

        while identificacion.strip() == "":
            print("Identificacion incorrecta")
            identificacion = input("Ingrese numero de identificacion: ")

        pais = int(input("Ingrese pais de destino entre 1 y 20: "))

        while pais < 1 or pais > 20:
            print("Pais incorrecto")
            pais = int(input("Ingrese pais de destino entre 1 y 20: "))

        asiento = int(input("Ingrese numero de asiento: "))

        while asiento <= 0:
            print("Asiento incorrecto")
            asiento = int(input("Ingrese numero de asiento: "))

        importe = int(input("Ingrese importe pagado: "))

        while importe <= 0:
            print("Importe incorrecto")
            importe = int(input("Ingrese importe pagado: "))

        tick = Ticket(codigo, identificacion, pais, asiento, importe)

        tickets.append(tick)

    return tickets


def mayor_asiento(tickets):
    num = int(input("Ingrese un numero: "))

    asientos_mayores = []

    # Filtrar
    for i in range(len(tickets)):
        if tickets[i].asiento > num:
            asientos_mayores.append(tickets[i])

    # Ordenar por codigo de vuelo
    for i in range(len(asientos_mayores)):
        for j in range(i + 1, len(asientos_mayores)):
            if asientos_mayores[i].codigo > asientos_mayores[j].codigo:
                asientos_mayores[i], asientos_mayores[j] = asientos_mayores[j], asientos_mayores[i]

    # Mostrar
    for i in range(len(asientos_mayores)):
        print(asientos_mayores[i])


def importes(tickets):

    print("-----------")
    valor_t = int(input("Ingrese un valor: "))

    acumulador = [0]*20

    for i in tickets:
        if i.pais >= 1 and i.pais <= 20:
            acumulador[i.pais - 1] += i.importe

    for i in range(len(acumulador)):
        if acumulador[i] > valor_t:
             print("Pais", i+1, "- Importe total:", acumulador[i])


def busqueda(tickets):
    id = input("Ingrese identificacion: ")
    encontrado = False

    for i in range(len(tickets)):
        if tickets[i].identificacion == id:
            print("Numero de asiento es: ", tickets[i].asiento)
            print("Su pais de destino es: ", tickets[i].pais)
            encontrado = True
            break
    if encontrado == False:
        print("No existe esa identificacion")
      
