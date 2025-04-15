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
