# Nicole Robles NC 0120
import pandas as pd

# Versión
print("Versión:", pd.__version__)

# Datos número 20 (según tu número de lista)
datos20 = {
    'distancia_km': [3.5, 1.2, 5.8, 2.3, 4.9],
    'trafico_nivel': [1, 3, 2, 1, 3],
    'edad_repartidor': [31, 25, 42, 28, 39],
    'tiempo_entrega_min': [24, 11, 48, 16, 46]
}

# 1. Explicación Didáctica de Conceptos (Estructura DataFrame y Series)
df = pd.DataFrame(datos20)
print("\n--- 1. Explicación Didáctica (DataFrame datos20) ---")
print(df)

# Columna individual (Serie)
serie_distancia = df['distancia_km']
print("\nSerie (distancia_km):")
print(serie_distancia)

# 2. Caso Práctico en Código (Inspección y Estadísticas)
print("\n--- 2. Caso Práctico (Info y Estadísticas) ---")
print(df.info())
print(df.describe())

# 3. Reto de Aprendizaje Basado en Problemas (ABP)
print("\n--- 3. Reto ABP (Verificación y Análisis) ---")
print("Valores nulos:")
print(df.isnull().sum())

print("\nFiltrado por tráfico alto (nivel 3):")
print(df[df['trafico_nivel'] == 3])

# Creación de variable calculada para resolver el reto
df['velocidad_km_h'] = df['distancia_km'] / (df['tiempo_entrega_min'] / 60)
print("\nResultado Final:")
print(df)
print("Nicole Robles NC 0120")