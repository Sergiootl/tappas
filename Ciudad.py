class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.restaurantes = []  # Lista de objetos Restaurante

    def agregar_restaurante(self, restaurante):
        self.restaurantes.append(restaurante)

    def obtener_restaurantes_por_plato(self, plato):
        return [rest for rest in self.restaurantes if rest.plato == plato]
