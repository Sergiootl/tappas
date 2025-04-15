# Documentación del Dataset "Restauración"

Este proyecto tiene como objetivo generar datos sintéticos a partir de un dataset original llamado `Restauracion.csv`, el cual contiene información sobre establecimientos de restauración en la región de Extremadura. El dataset original fue descargado de [datos.gob.es](https://datos.gob.es/es/catalogo/a11002926-establecimientos-de-restauracion-en-extremadura).

Para crear los datos sintéticos que utilizaremos posteriormente en nuestra aplicación, hemos añadido tres columnas adicionales al dataset: **Platos**, **Mejores platos** y **Valoración**. Estas columnas se han generado de manera que los datos resultantes sean lo más realistas posible, siguiendo las características del sector de la restauración en Extremadura.

A continuación, se detalla la información sobre cada columna y sus valores posibles.

## 1. **Provincia**
- **Descripción**: Provincia en la que se encuentra el establecimiento.
- **Tipo de dato**: Texto.
- **Valores posibles**:  
  - Badajoz  
  - Cáceres

## 2. **Modalidad**
- **Descripción**: Tipo de establecimiento según su modalidad de servicio.
- **Tipo de dato**: Texto.
- **Valores posibles**:  
  - Restaurante  
  - Cafetería  
  - Café - Bar  
  - Pub  
  - Catering  
  - Salón de banquetes y convenciones  
  - Discoteca  

## 3. **Tipo de recurso**
- **Descripción**: Clasificación según el tipo de recurso del establecimiento.
- **Tipo de dato**: Texto.
- **Valores posibles**:  
  - I (para Café - Bar)  
  - II (para Restaurante, Salón de banquetes y convenciones y Catering)  
  - III (para Pub y Discoteca)  

## 4. **Categoría**
- **Descripción**: Clasificación del establecimiento según su nivel o tipo, dependiendo de la modalidad.
- **Tipo de dato**: Texto.
- **Valores posibles**:  
  **Restaurantes**:  
  - 1 tenedor  
  - 2 tenedores  
  - 3 tenedores  
  - 4 tenedores  
  **Cafeterías**:  
  - 1 taza  
  - 2 tazas  
  - 3 tazas  
  **Salón de banquetes y convenciones**:  
  - Básico  
  - Medio  

## 5. **Fecha de apertura**
- **Descripción**: Fecha en la que el establecimiento abrió sus puertas.
- **Tipo de dato**: Fecha.
- **Formato**: `AAAA-MM-DD`.
- **Ejemplo**: 1990-09-20

## 6. **Nombre del establecimiento**
- **Descripción**: Nombre comercial del establecimiento.
- **Tipo de dato**: Texto.
- **Ejemplo**: THE FOOD WAY

## 7. **Municipio**
- **Descripción**: Municipio donde se localiza el establecimiento.
- **Tipo de dato**: Texto.
- **Ejemplo**: ACEUCHAL

## 8. **Dirección**
- **Descripción**: Dirección del establecimiento.
- **Tipo de dato**: Texto.
- **Ejemplo**: PLAZA CONSTITUCIÓN, 17

## 9. **Código Postal**
- **Descripción**: Código postal correspondiente a la dirección del establecimiento.
- **Tipo de dato**: Entero.
- **Ejemplo**: 6207

## 10. **Web**
- **Descripción**: Dirección web del establecimiento.
- **Tipo de dato**: Texto.
- **Valores posibles**:  
  - SI  
  - NO

## 11. **Nº Plazas**
- **Descripción**: Número de plazas disponibles en el establecimiento. Si se desconoce, se indica 0.
- **Tipo de dato**: Entero.
- **Ejemplo**: 50

## 12. **Platos**
- **Descripción**: Lista de los 15 platos que se sirven en el establecimiento.
- **Tipo de dato**: Texto.
- **Ejemplo**: Tortilla de patatas, Migas extremeñas, Callos, Chanfaina, Patatas bravas, Lomo adobado, Morcilla patatera, Queso de la Serena, Jamón ibérico, Croquetas caseras, Carrillada ibérica, Pincho moruno, Calamares fritos, Montadito de secreto, Gazpacho extremeño

## 13. **Mejores platos**
- **Descripción**: Los 5 mejores platos del establecimiento, elegidos de manera aleatoria.
- **Tipo de dato**: Texto.
- **Ejemplo**: Queso de la Serena, Callos, Jamón ibérico, Tortilla de patatas, Chanfaina

## 14. **Valoración**
- **Descripción**: Valoración del establecimiento, en una escala del 0 al 5, elegida de manera aleatoria con un decimal.
- **Tipo de dato**: Decimal.
- **Ejemplo**: 4,1

---
# Script de Asignación de Platos por Establecimiento en Python

## Objetivo del Script
Este script tiene como objetivo asignar platos representativos a los establecimientos de restauración de un archivo CSV (`Restauracion.csv`). Los platos se asignan basándose en la **modalidad** (Restaurante, Cafetería, Café-Bar), la **categoría** (tenedores/tazas) y las **palabras clave** en el nombre del establecimiento. El resultado final se guarda en un archivo Excel denominado `Restauracion_con_platos.xlsx`.

## Pasos Principales del Script

1. **Importación de Librerías**  
   Utilizamos:
   - `pandas`: para manejar el archivo CSV y manipular datos.
   - `chardet`: para detectar la codificación del archivo CSV.
   - `random`: para seleccionar platos aleatorios.
   - `Enum`: para definir categorías de establecimientos.

2. **Enumeraciones para Categorías**  
   Definimos clases de enumeración (`Enum`) para categorizar los restaurantes y cafeterías por su nivel (ej. 1 tenedor, 2 tenedores, etc.).

3. **Diccionarios de Platos por Categoría**  
   Creamos diccionarios que asignan listas de platos dependiendo de la categoría del establecimiento (Restaurante de 1 tenedor, 4 tenedores, Cafeterías, etc.).

4. **Palabras Clave en el Nombre del Establecimiento**  
   Definimos un diccionario que asigna platos según palabras clave en el nombre del establecimiento (por ejemplo, "sushi", "mexican", "burger").

5. **Lectura del CSV y Detección de Codificación**  
   Leemos el archivo CSV (`Restauracion.csv`), detectamos su codificación para asegurar que se carga correctamente y lo transformamos a formato .xlsx para poder trabajar mejor con pandas.

6. **Lógica de Asignación de Platos**  
   Según la modalidad del establecimiento, la categoría y las palabras clave en el nombre, se asignan entre 3 a 5 platos aleatorios. El código verifica estas condiciones y asigna los platos correspondientes.
   
7. **Exportación de Datos**  
Finalmente, se agregan los platos asignados al DataFrame y el resultado final se guarda en un archivo Excel denominado `Restauracion_con_platos.xlsx`
