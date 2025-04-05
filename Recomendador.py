class Recomendador:
    def __init__(self):
        pass

    def recomendar(self, ciudad, plato):
        restaurantes = ciudad.obtener_restaurantes_por_plato(plato)
        # Ordenar por la valoración
        restaurantes_ordenados = sorted(restaurantes, key=lambda x: x.valoracion, reverse=True)
        return restaurantes_ordenados[:3]  # Devolver los tres mejores
