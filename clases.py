class Objetos:
    def __init__(self, codigo, nombre, servicio, importe):
        self.codigo = codigo
        self.nombre = nombre
        self.servicio = servicio
        self.importe = importe

    def __str__(self) :
        return(
            "Codigo identificatorio: " + str(self.codigo)+
            "- Nombre del cliente: " + self.nombre+
            "- Tipo de servicio: " + str(self.servicio)+
            "- Importe: " + str(self.importe)

        )
