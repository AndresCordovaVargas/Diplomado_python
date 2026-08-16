Dados= {
    "Producto":["Lampara", "Desarmador", "Autocle", "Llaves"]
    "Precio":[60, 200, 1000, 500]
    "Existencia":[30, 20, 10, 8]
}
# 1.- Mostrar la columna Precio.
print("Columna precio:")
print(Fr["Precio"])
print("\n"+"="*40+"\n")

# 2.- Mostrar productos con precio mayor a 500.
print("Productos con precio mayor a $500:")
print(Fr[Fr["Precio"]>500])
print("\n"+"="*40+"\n")

# 3.- Crear columna IVA.
Fr["IVA"]"Fr["Precio"]*0.16
print("Columna IVA:")
print(Fr)
print("\n"+"="*40+"\n")

# 4.- Crear la columna precio final.
Fr["Precio final"]=Fr["Precio"]+Fr["iIVA"]
print("Precio final:")
print(Fr)
print("\n"+"="*40+"\n")

# 5.- Mostrar unucamente los productos con existencia menor a 10.
print("Productos existentes")
print(Fr[Fr["Existencia"]<10])

