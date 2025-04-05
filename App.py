class App:
    def __init__(self, api_key):
        self.base_datos = BaseDatos()
        self.recomendador = Recomendador()
        self.ruta = Ruta(api_key)

    def iniciar(self):
        # Pedir datos al usuario
        ciudad_input = input("Introduce la ciudad: ")
        plato_input = input("Introduce el plato: ")

        # Verificar si los datos están en Redis
        clave = f"{ciudad_input}-{plato_input}"
        restaurantes_en_cache = self.base_datos.obtener_restaurantes_desde_redis(clave)

        if restaurantes_en_cache:
            print("Datos obtenidos desde cache.")
            restaurantes = restaurantes_en_cache
        else:
            print("Consultando base de datos...")
            # Obtener restaurantes de MongoDB (o puedes hacerlo desde otro lugar)
            ciudad = Ciudad(ciudad_input)
            restaurantes = self.base_datos.obtener_restaurantes_desde_mongo(ciudad_input)
            for rest in restaurantes:
                restaurante = Restaurante(rest["nombre"], rest["ciudad"], rest["plato"], rest["valoracion"], rest["direccion"])
                ciudad.agregar_restaurante(restaurante)

            # Guardar en Redis para futuras consultas
            self.base_datos.guardar_en_redis(clave, restaurantes)
        
        # Recomendación de los mejores restaurantes
        restaurantes_recomendados = self.recomendador.recomendar(ciudad, plato_input)

        # Mostrar los resultados
        for restaurante in restaurantes_recomendados:
            print(restaurante)

        # Obtener la mejor ruta a cada restaurante
        for restaurante in restaurantes_recomendados:
            print(f"Mejor ruta a {restaurante.nombre}:")
            ruta = self.ruta.obtener_mejor_ruta(ciudad_input, restaurante.direccion)
            print(f"Tiempo estimado: {ruta[0]}, Distancia: {ruta[1]}")
