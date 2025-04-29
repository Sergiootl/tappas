import pandas as pd
import chardet
import random
from enum import Enum

# Definimos los enumeradores para las categorías de restaurante y cafetería
class CategoriaRestaurante(Enum):
    CATEGORIA_4_TENEDORES = "4 Tenedores"
    CATEGORIA_3_TENEDORES = "3 Tenedores"
    CATEGORIA_2_TENEDORES = "2 Tenedores"
    CATEGORIA_1_TENEDOR = "1 Tenedor"

class CategoriaCafeteria(Enum):
    CATEGORIA_3_TAZAS = "3 Tazas"
    CATEGORIA_2_TAZAS = "2 Tazas"
    CATEGORIA_1_TAZA = "1 Taza"

# Diccionario de platos por categoría
platos_por_categoria = {
    '1 tenedor': ["Jamón Ibérico","Lomo Ibérico","Queso curado","Ensalada mixta","Gazpacho","Croquetas caseras","Patatas bravas","Secreto Ibérico con patatas","Solomillo de ternera con patatas","Bocadillo de lomo","Empanada de atún","Sopa de ajo","Pluma Ibérica con patatas","Tarta de manzana","Flan casero"],
    '2 tenedores': ["Lomo Ibérico con tomate","Ensalada de pimientos asados","Tartar de atún","Revuelto de setas","Migas Extremeñas","Tacos de cochinillo","Pollo al ajillo","Estofado de ternera","Bacalao dorado","Pisto con huevo","Lomos de sardina a la parrilla","Tartar de tomate y mozzarella","Tarta de queso con frutos rojos","Arroz con bogavante","Tarta de almendra"],
    '3 tenedores': ["Cordero a la parrilla con patatas","Tartar de aguacate con langostinos","Carne de retinto a la brasa","Ceviche de dorada","Merluza de pincho con salsa de cítricos","Arroz meloso con setas y trufa","Rabo de toro estofado","Pichón asado con puré de castañas","Foie gras con reducción de vino de pitarra","Piquillos rellenos de merluza","Tarta de chocolate y avellanas","Mousse de mango y maracuyá","Helado casero de lavanda","Pato confitado con salsa de frutos rojos","Tarta de limón con base de galleta"],
    '4 tenedores': ["Caviar de trucha con crema de queso y pan de cristal","Carne de retinto a la parrilla con emulsión de ajo negro","Bacalao confitado con salsa de pimientos asados","Atún rojo con ensalada de alga wakame y soja","Tartar de buey con yema de huevo de corral","Ravioli de calabaza con mantequilla de trufa","Tartar de langosta con aguacate y vinagreta de frambuesa","Lomo de venado con puré de patatas trufado","Tarta de foie gras con reducción de Pedro Ximénez","Pato a la naranja con ensalada de cebolla morada","Risotto de setas de temporada con trufa negra","Sopa de mariscos con toque de jengibre y limón","Postre de chocolate, frutos rojos y gelatina de cava","Piquillos rellenos de brandada de bacalao","Helado de aceite de oliva virgen extra con sal Maldon"],
    '1 taza': ["Café Solo","Café con Leche","Tostadas con Tomate","Café con leche condensada","Bollería variada","Galletas caseras","Bizcocho de yogur","Croissant","Bocadillo de jamón y queso","Pan con aceite de oliva y tomate","Café de máquina","Magdalenas","Panecillos rellenos de chocolate","Bocadillo de calamares","Churros con chocolate"],
    '2 tazas': ["Café Americano","Café Cortado","Bocadillo de Jamón","Croissant","Bocadillo de Queso Manchego","Tarta de manzana","Bocadillo de tortilla","Café con leche de avena","Bollos suizos","Café con leche de soja","Tarta de zanahoria","Galletas de avena y miel","Tostada con aguacate y huevo poché","Café con leche y un toque de vainilla","Muffins de arándano"],
    '3 tazas': ["Café Espresso","Tarta de Manzana","Bocadillo de Tortilla","Café Latte","Café Mocha","Tarta de almendra","Tarta de limón y merengue","Café Macchiato","Croissant relleno de crema de pistacho","Bocadillo de jamón ibérico y tomate","Bollería artesana","Tarta de chocolate con frutos rojos","Bizcocho de almendra y miel","Tarta de mousse de chocolate","Café irlandés","Galletas de chocolate blanco y macadamia"]
}


# Diccionario de platos para Café - Bar
platos_por_cafe_bar = {
    'cafe-bar': [
        'Tortilla de patatas','Migas extremeñas','Callos','Chanfaina','Patatas bravas','Lomo adobado','Morcilla patatera','Queso de la Serena','Jamón ibérico','Croquetas caseras','Carrillada ibérica','Pincho moruno','Calamares fritos','Montadito de secreto','Gazpacho extremeño'
    ]
}


# Diccionario de palabras clave en nombres y sus platos asociados
platos_por_nombre_clave = {
'mexican': ["Tacos al Pastor","Guacamole con Totopos","Enchiladas Verdes","Fajitas de Pollo","Quesadillas de Champiñones","Tamales de Elote","Tostadas de Tinga de Pollo","Chiles en Nogada","Pozole Rojo","Sopes de Carne","Burritos de Carne Asada","Tacos de Carnitas","Mole Poblano","Tacos de Pescado","Churros con Chocolate"],
'sushi': ["Sushi de Salmón","Nigiri de Atún","Sashimi de Pargo","Tempura de Verduras","Maki de Aguacate y Pepino","California Roll","Dragon Roll","Tuna Tataki","Ebi Tempura Roll","Tartar de Atún","Sushi de Langostino","Sushi de Pargo","Sushi Vegetariano","Maki de Salmón y Palta","Tamago (Tortilla japonesa)"],
'ital': ["Spaghetti a la Bolognesa","Lasagna Tradicional","Pizza Margherita","Risotto de Setas","Gnocchi al Pesto","Ravioli de Espinacas y Ricotta","Focaccia de Romero","Pasta Carbonara","Fettuccine Alfredo","Bruschetta con Tomate y Albahaca","Pizza Cuatro Estaciones","Tiramisu","Penne Arrabbiata","Pollo a la Cacciatora","Cannoli Siciliani"],
'asia': ["Sushi de Salmón","Dumplings al Vapor","Ramen Tonkotsu","Tempura de Calamares","Spring Rolls de Verduras","Pho de Pollo","Pad Thai","Satay de Pollo","Arroz Frito con Verduras","Katsu Curry","Gyoza de Cerdo","Ternera al Curry","Kimchi","Bao Buns de Cerdo","Szechuan Chicken"],
'grill': ["Costillas a la Barbacoa","Hamburguesa Gourmet con Queso Cheddar","Pollo a la Parrilla","Pinchos Morunos","Chuletones a la Parrilla","Entrecot a la Plancha","Lomo de Cerdo a la Brasa","Burgers de Pollo","Costillas de Cerdo","Salchichas al Grill","Brochetas de Cordero","Pechuga de Pollo con Hierbas","Cordero a la Parrilla","Lasaña de Carne","Salmón a la Parrilla"],
'pizza': ["Pizza Margherita","Pizza Pepperoni","Pizza Hawaiana","Pizza Vegetariana","Pizza Cuatro Quesos","Pizza Pollo al Pesto","Pizza de Jamón y Champiñones","Pizza Mexicana","Pizza Napolitana","Pizza de Carne Asada","Pizza de Mariscos","Pizza Calzone","Pizza de Espinacas y Ricotta","Pizza de Atún y Cebolla","Pizza Diavola"],
'burger': ["Hamburguesa Clásica","Cheese Burger","Bacon Burger","Veggie Burger","BBQ Burger","Chili Burger","Mushroom Swiss Burger","Classic Chicken Burger","Avocado Burger","Double Cheeseburger","Tex-Mex Burger","Chicken Tender Burger","Pulled Pork Burger","Steak Burger","Spicy Jalapeño Burger"],
'seafood': ["Paella Valenciana","Mariscada a la Parrilla","Mejillones a la Marinera","Almejas a la Plancha","Langostinos a la Brasa","Arroz Negro con Calamares","Bacalao a la Vizcaína","Lubina a la Sal","Pulpo a la Gallega","Calamares Rellenos","Sopa de Marisco","Tartar de Atún","Arroz Caldoso de Mariscos","Salmón a la Parrilla","Tartar de Salmón"],
'vegetarian': ["Ensalada Mediterránea","Hummus con Pan de Pita","Tofu a la Parrilla","Veggie Burger","Pasta Vegana","Falafel con Salsa de Yogur","Ensalada de Quinoa","Buddha Bowl","Acelgas Rellenas","Sopa de Lentejas","Tabulé","Lasagna Vegetariana","Pizza Vegetariana","Tarta de Zanahoria","Moussaka Vegetariana"]
}


# Detectar codificación del archivo CSV
csv_file = 'Restauracion.csv'
excel_file = 'Restauracion.xlsx'

with open(csv_file, 'rb') as f:
    result = chardet.detect(f.read())
encoding_detectado = result['encoding']
print(f"Codificación detectada: {encoding_detectado}")

# Leer y convertir CSV a Excel
df = pd.read_csv(csv_file, encoding=encoding_detectado, sep=',')
df.to_excel(excel_file, index=False)
print(f"Archivo convertido a Excel: '{excel_file}'")

# Leer Excel
df = pd.read_excel(excel_file)

# Mapas de categorías
categoria_restaurante_map = {
    '1 Tenedor': CategoriaRestaurante.CATEGORIA_1_TENEDOR,
    '2 Tenedores': CategoriaRestaurante.CATEGORIA_2_TENEDORES,
    '3 Tenedores': CategoriaRestaurante.CATEGORIA_3_TENEDORES,
    '4 Tenedores': CategoriaRestaurante.CATEGORIA_4_TENEDORES
}

categoria_cafeteria_map = {
    '1 Taza': CategoriaCafeteria.CATEGORIA_1_TAZA,
    '2 Tazas': CategoriaCafeteria.CATEGORIA_2_TAZAS,
    '3 Tazas': CategoriaCafeteria.CATEGORIA_3_TAZAS
}

# Asignar platos por nombre del establecimiento
def asignar_platos_por_nombre(nombre_establecimiento):
    if isinstance(nombre_establecimiento, str):
        nombre_establecimiento = nombre_establecimiento.lower()
        for palabra_clave, platos in platos_por_nombre_clave.items():
            if palabra_clave in nombre_establecimiento:
                return ','.join(platos)
    return ''

# Asignar platos según categoría restaurante
def asignar_platos_restaurante(categoria_restaurante):
    if categoria_restaurante == CategoriaRestaurante.CATEGORIA_1_TENEDOR:
        return ','.join(platos_por_categoria['1 tenedor'])
    elif categoria_restaurante == CategoriaRestaurante.CATEGORIA_2_TENEDORES:
        return ','.join(platos_por_categoria['2 tenedores'])
    elif categoria_restaurante == CategoriaRestaurante.CATEGORIA_3_TENEDORES:
        return ','.join(platos_por_categoria['3 tenedores'])
    elif categoria_restaurante == CategoriaRestaurante.CATEGORIA_4_TENEDORES:
        return ','.join(platos_por_categoria['4 tenedores'])
    return ''

# Asignar platos según categoría cafetería
def asignar_platos_cafeteria(categoria_cafeteria):
    if categoria_cafeteria == CategoriaCafeteria.CATEGORIA_1_TAZA:
        return ','.join(platos_por_categoria['1 taza'])
    elif categoria_cafeteria == CategoriaCafeteria.CATEGORIA_2_TAZAS:
        return ','.join(platos_por_categoria['2 tazas'])
    elif categoria_cafeteria == CategoriaCafeteria.CATEGORIA_3_TAZAS:
        return ','.join(platos_por_categoria['3 tazas'])
    return ''

def asignar_platos_cafe_bar():
    return ','.join(platos_por_cafe_bar['cafe-bar'])

# Función para seleccionar los mejores platos (máximo 5 aleatorios)
def seleccionar_mejores_platos(platos_str):
    if isinstance(platos_str, str) and platos_str.strip():
        platos_list = [plato.strip() for plato in platos_str.split(',')]
        return ','.join(random.sample(platos_list, min(5, len(platos_list))))
    return ''

# Diccionario que almacena ratings previos: {("Ciudad", "Plato"): set(ratings)}
valoraciones_por_plato_ciudad = {}

def generar_valoracion(nombre_local, municipio, mejores_platos):
    intentos = 0
    max_intentos = 50
    while intentos < max_intentos:
        rating = round(random.uniform(2.5, 5.0), 1)
        conflicto = False

        # Verificamos si el plato en el municipio ya tiene el mismo rating
        for plato in mejores_platos.split(','):  # Asegurándonos de que los platos están en formato lista
            clave = (municipio, plato.strip())
            if clave in valoraciones_por_plato_ciudad and rating in valoraciones_por_plato_ciudad[clave]:
                conflicto = True
                break
        
        if not conflicto:
            # Si no hay conflicto, registramos el rating
            for plato in mejores_platos.split(','):
                clave = (municipio, plato.strip())
                if clave not in valoraciones_por_plato_ciudad:
                    valoraciones_por_plato_ciudad[clave] = set()
                valoraciones_por_plato_ciudad[clave].add(rating)
            return rating
        
        intentos += 1

    # Si no encuentra un rating único tras varios intentos, lo retorna de todas formas
    return rating

# Función para asignar la valoración correctamente a cada fila de tu DataFrame
def asignar_rating(row):
    mejores_platos = row['Mejores platos']
    municipio = row['Municipio']  # Asegúrate de que tienes la columna 'Municipio'
    nombre_local = row['Nombre establecimiento']  # Asegúrate de que tienes la columna 'Nombre establecimiento'
    
    return generar_valoracion(nombre_local, municipio, mejores_platos)

# Función principal: orden de prioridad → nombre > modalidad/categoría
def asignar_platos(row):
    try:
        # 1. Comprobamos si el nombre del establecimiento contiene palabras clave
        platos_nombre = asignar_platos_por_nombre(row['Nombre establecimiento'])
        if platos_nombre:
            return platos_nombre
        
        # 2. Si no hay coincidencia por nombre, vamos a modalidad y categoría
        modalidad = str(row['Modalidad'])
        categoria = row['Categoría']

        if 'Restaurante' in modalidad:
            categoria_restaurante = categoria_restaurante_map.get(categoria)
            if categoria_restaurante:
                return asignar_platos_restaurante(categoria_restaurante)

        elif 'Cafetería' in modalidad:
            categoria_cafeteria = categoria_cafeteria_map.get(categoria)
            if categoria_cafeteria:
                return asignar_platos_cafeteria(categoria_cafeteria)

        elif 'Café - Bar' in modalidad:
            return asignar_platos_cafe_bar()

        elif 'Salón de banquetes' in modalidad or 'Catering' in modalidad:
            return "Menú con reserva previa"

        return ''
    except Exception as e:
        print(f"Error en asignar_platos: {e}")
        return ''

# Normalizamos la columna 'Municipio' a mayúsculas para evitar duplicados
df['Municipio'] = df['Municipio'].str.upper()

# Crear la columna 'Platos' utilizando la función principal
df['Platos'] = df.apply(asignar_platos, axis=1)

# Crear la columna 'Mejores platos' seleccionando 5 platos aleatorios
df['Mejores platos'] = df['Platos'].apply(seleccionar_mejores_platos)

# Crear la columna 'Rating' generando una valoración aleatoria entre 2.5 y 5, garantizando que no se repita
df['Rating'] = df.apply(asignar_rating, axis=1)

# Guardar el DataFrame con las nuevas columnas
df.to_excel('Restauracion_con_platos.xlsx', index=False)
print("Archivo final guardado como 'Restauracion_con_platos.xlsx'")