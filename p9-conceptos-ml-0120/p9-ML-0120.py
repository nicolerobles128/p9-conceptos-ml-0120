# Nicole Robles NC 0120
import pandas as pd

# Versión
print(pd.__version__)

# Datos #20
datos20 = {
    'distancia_km': [3.5, 1.2, 5.8, 2.3, 4.9],
    'trafico_nivel': [1, 3, 2, 1, 3],
    'edad_repartidor': [31, 25, 42, 28, 39],
    'tiempo_entrega_min': [24, 11, 48, 16, 46]
}

# DataFrame
df = pd.DataFrame(datos20)

# Punto 2: Caso Práctico
print(df)
print(df.info())
print(df.describe())

# Punto 3: Reto ABP
print(df.isnull().sum())
print(df[df['trafico_nivel'] == 3])

df['velocidad_km_h'] = (df['distancia_km'] / (df['tiempo_entrega_min'] / 60))
print(df)
print("Nicole Robles NC 0120")