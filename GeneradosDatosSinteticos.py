import pandas as pd
import numpy as np

def cargar_datos(ruta_excel):
    """Carga el dataset desde un archivo Excel."""
    return pd.read_excel(ruta_excel)

def generar_datos_sinteticos(df):
    """Genera datos sintéticos según patrones específicos."""
    # Aquí podemos definir reglas para los datos sintéticos
    df_sintetico = df.copy()
    
    # Ejemplo: Si hay una columna 'edad', generamos edades entre 20 y 60
    if 'edad' in df_sintetico.columns:
        df_sintetico['edad'] = np.random.randint(20, 60, size=len(df_sintetico))
    
    return df_sintetico

def agregar_datos_aleatorios(df, enumerador):
    """Añade valores aleatorios basados en un enumerador proporcionado."""
    df_aleatorio = df.copy()
    
    for columna, valores in enumerador.items():
        if columna in df_aleatorio.columns:
            df_aleatorio[columna] = np.random.choice(valores, size=len(df_aleatorio))
    
    return df_aleatorio

def guardar_datos(df, ruta_salida):
    """Guarda el dataset modificado en un archivo Excel."""
    df.to_excel(ruta_salida, index=False)

# Uso del programa
ruta_entrada = "dataset.xlsx"  # Ruta del archivo original
ruta_salida = "dataset_sintetico.xlsx"  # Ruta para guardar el dataset final
enumerador = {
    "categoria": ["A", "B", "C", "D"],  # Ejemplo de enumerador
}

df_original = cargar_datos(ruta_entrada)
df_sintetico = generar_datos_sinteticos(df_original)
df_final = agregar_datos_aleatorios(df_sintetico, enumerador)
guardar_datos(df_final, ruta_salida)

print("Proceso completado. Datos sintéticos generados y guardados.")
