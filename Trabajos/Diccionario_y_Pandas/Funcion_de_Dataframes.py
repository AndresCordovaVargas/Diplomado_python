import pandas as pd
empleados = pd. DataFrame ({
    "ID": [1, 2, 3, 4, 5],
    "Nombre": ["Ana", "Luis", "Pedro", "Marta", "Jorge"],
    "ID_Depto": [10, 20, 10, 30, 20],
    "Salario_Base": [25000, 32000, 28000, 45000, 31000]
})
departamentos = pd. DataFrame ({
    "ID_Depto": [10, 20, 30],
    "Departamento": ["Sistemas", "Ventas", "Direccion"],
    "Bono_Porcentaje": [0.15, 0.25, 0.30]
})
df_fusionado = pd.merge(empleados, departamentos, on="ID_Depto")

df_fusionado["Salario_Neto"] = df_fusionado["Salario_Base"] + (df_fusionado["Salario_Base"] * df_fusionado["Bono_Porcentaje"])
empleados_filtrados = df_fusionado[df_fusionado["Salario_Neto"] > 35000]
empleados_filtrados.to_csv("empleados_destacados.csv", sep=";", index=False)
print("---Dataframe Fusionado y con Salario Neto---")
print(df_fusionado)
print("\n---Empleados con Salario Neto superior a 35000 (Filtro)---")
print(empleados_filtrados)
print("\n¡Archivo empleados_destacados.csv creado con exito!")
