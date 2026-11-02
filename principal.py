
class Perceptron:
    def __init__(self, w0, w1, umbral, desc="P"):
        self.w0 = w0
        self.w1 = w1
        self.umbral = umbral
        self.descripcion = desc
        self.resultados = []

    def __str__(self):
        r = f"Perceptrón: {self.descripcion} - (W0: {self.w0} - W1: {self.w1} - Umbral: {self.umbral})"
        return r

    def activar(self, x0, x1):
        s = self.w0 * x0 + self.w1 * x1

        if s > self.umbral:
            resultado = 1
        else:
            resultado = 0

        self.resultados.append(resultado)
        return resultado

    

def calcular_r1(p4):
    contador = 0

    for i in p4.resultados:
        if i == 1:
            contador += 1

    print("r1:", contador)

def calcular_r2(p):
    contador = 0

    for i in p:
        for resultado in i.resultados:
            if resultado == 1:
                contador += 1
    
    return contador

def calcular_r3(p):
    for i in range(20):
        for j in range(len(p)):
            if p[j].resultados[i] == 1:
                return j

    return -1 


def calcular_r4(p):
    r4 = -1

    for i in range(len(p[0].resultados)):
        contador = 0

        for j in range(len(p)):
            if p[j].resultados[i] == 0:
                contador += 1

        if contador == len(p):
            r4 = i

    return r4


p0 = Perceptron(1, 2, 1, "P0")
p1 = Perceptron(1, 1, 2, "P1")
p2 = Perceptron(3, 1, 3, "P2")
p3 = Perceptron(2, 1, 3, "P3")
p4 = Perceptron(1, 1, 1, "P4")

p = [p0, p1, p2, p3, p4]


entradas = [
    [(0, 0), (0, 1)],
    [(1, 0), (1, 1)],
    [(1, 2), (2, 1)],
    [(0, 2), (2, 2)],
    [(2, 0), (2, 3)],
    [(3, 2), (0, 3)],
    [(3, 0), (3, 3)],
    [(2, 4), (4, 2)],
    [(4, 4), (0, 4)],
    [(4, 0), (1, 5)],
    [(5, 1), (5, 5)],
    [(0, 5), (5, 0)],
    [(6, 6), (4, 6)],
    [(2, 6), (6, 2)],
    [(7, 6), (7, 7)],
    [(2, 5), (3, 5)],
    [(5, 2), (5, 3)],
    [(3, 6), (0, 3)],
    [(1, 7), (2, 1)],
    [(0, 2), (3, 7)]
]

columna1 = []
columna2 = []

for fila in entradas:
    columna1.append(fila[0])
    columna2.append(fila[1])



for i in range(20):

    fila = columna1[i]
    s0 = p0.activar(fila[0], fila[1])

    fila2 = columna2[i]
    s1 = p1.activar(fila2[0], fila2[1])

    s2 = p2.activar(s0, s1)

    s3 = p3.activar(fila2[0], fila2[1])

    s4 = p4.activar(s2, s3)


r1 = calcular_r1(p4)

r2 = calcular_r2(p)
print("R2:", r2)

r3 = calcular_r3(p)
print("R3:", r3)

r4 = calcular_r4(p)
print("R4:", r4)