#Limpieza y Agregacion con Pandas.
import pandas as pd
import numpy as np
datos_ventas = {
"Sucursal": ["Norte", "Sur", "Norte", "Centro", "Sur", "Centro", "Norte"], "Vendedor": ["Carlos", "Maria", "Jorge", "Ana", np.nan, "Luis", "Elena"],
"Ventas": [15000, 22000, np.nan, 18000, 25000, np.nan, 17500],
"Clientes": [15, 20, 12, 18, 25, 14, 16]
}
df_ventas = pd.DataFrame(datos_ventas)

# 1.- Rellena los valores nulos de la columna Ventas con la mediana de las ventas totales.

media_ventas = df_ventas["Ventas"].median()
df_ventas["Ventas"] = df_ventas["Ventas"].fillna(mediana_ventas)

# 2.- Elimina las filas donde el nombre del Vendedor sea un valor nulo.

df_ventas = df_ventas.dropna("Sucursal").agg(
    Total_Ventas=("Ventas", "sum"),
    Promedio_Clientes=("Clientes", "mean")
).reset_index()

# 3.- Agrupar los datos por Sucursal y calcula el total de Ventas y el promedio de Clientes por sucursal.

print("---DataFrame despues de la limpieza---")
print(df_ventas)
print("\n---Resultado de la Agregacion ---")
print(resultado)
