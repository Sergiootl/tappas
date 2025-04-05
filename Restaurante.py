class Restaurante:
    def __init__(self, nombre, ciudad, plato, valoracion, direccion):
        self.nombre = nombre
        self.ciudad = ciudad
        self.plato = plato
        self.valoracion = valoracion
        self.direccion = direccion

    def __str__(self):
        return f"{self.nombre} - {self.plato} - Valoración: {self.valoracion}"
