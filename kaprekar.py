def krapekar():
    numero = input("Ingrese un número de 4 dígitos: ")

    digitos = list(numero)
    digitos2 = digitos[:]

    contador = 0 
    bandera = False
    lol = 0
    c1 = 0

    for x  in digitos:
        if bandera == False:
            lol = x
            bandera = True
        else:
            if lol == x:
                c1 += 1

    

    if len(digitos) == 4 and c1 != 4:
     while True:   
        if numero == "6174":
            print("Se ha llegado a la constante de Kaprekar: 6174")
            break

        else:
            # ASCENDENTE
            for i in range(len(digitos)):
                for j in range(i + 1, len(digitos)):
                    if digitos[i] > digitos[j]:
                        digitos[i], digitos[j] = digitos[j], digitos[i]

            ascendente = (
                int(digitos[0]) * 1000
                + int(digitos[1]) * 100
                + int(digitos[2]) * 10
                + int(digitos[3])
            )

            # DESCENDENTE
            for i in range(len(digitos2)):
                for j in range(i + 1, len(digitos2)):
                    if digitos2[i] < digitos2[j]:
                        digitos2[i], digitos2[j] = digitos2[j], digitos2[i]

            descendente = (
                int(digitos2[0]) * 1000
                + int(digitos2[1]) * 100
                + int(digitos2[2]) * 10
                + int(digitos2[3])
            )

            resultado = descendente - ascendente
            contador += 1
            numero = str(resultado)
            digitos = list(numero)
            digitos2 = digitos[:]

            print("Ascendente:", ascendente)
            print("Descendente:", descendente)
            print("Resultado:", resultado)
            print("Vueltas:", contador)


krapekar()