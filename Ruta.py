import requests  # Para hacer peticiones a Google Maps API o OpenStreetMap

class Ruta:
    def __init__(self, api_key):
        self.api_key = api_key  # Necesitas una API key de Google Maps o usar otra API

    def obtener_mejor_ruta(self, origen, destino):
        # Este es un ejemplo usando Google Maps API
        url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origen}&destination={destino}&key={self.api_key}"
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'OK':
            # Procesar la respuesta y devolver la mejor ruta
            ruta = data['routes'][0]['legs'][0]
            return ruta['duration']['text'], ruta['distance']['text']
        else:
            return None
