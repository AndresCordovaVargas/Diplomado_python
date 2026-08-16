import pandas as pd
df=pd.read_csv("ecommerce_data.csv")
print("\n---primeras 10 y ultimas 5 filas---\n")
print(df.head(10))
print(df.tail(5))
# 3.- Mostrar las ultimas 5 columnas
print("\n---ultimas 5 columnas---\n")
print(df.iloc[:, -5:])

# 4.- Obtener dimenciones (filas, columnas)
print("\n---dimenciones del dataset---\n")
print(df.shape)

# 5.- Mostrar las columnas
print("\n---Nombres de las columnas---\n")
print(df.columnas)

# 6.- Mostrar los tipos de datos
print("\n---Tipos de datos de las columnas---\n")
print(df.dtypes)
# Ejercicio numero 2
#1.- Mostrar las primeras dies filas
print("\n---primeras 10 filas---\n")
print(df.head(10))
# 2.- Calcular el gasto promedio
gasto_promedio=df["Total_gastado"].mean()
print(f"\nEl gasto promedio es: {gasto_promedo}")
# 3.- identificar el gasto maximo
gasto_maximo=df["Total_gastado"].max()
print(f"El gasto maximo es: {gasto_maximo}")

