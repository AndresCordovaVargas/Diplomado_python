import random
def simular_Lanzamientos(s):
    eventos = ["Aguila", "Sol"]
    resultados = [random.choice(evevtos) for_in range(s)]

print(f"---Resultaods de 5 lanzamientos de una moneda---")
for i, resultado in enumerate(resultados,1):
    print(f"Lanzamiento {1}: {resultado}")

    Aguila = resultados.count("Aguila")
    Sol = resultados.count("Sol")
    print(f"Lanzamientos de Aguilas: {Aguila} | Total de Soles: {Sol}")
    