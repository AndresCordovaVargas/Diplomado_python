import random
def simular_Lanzamientos(s):
    eventos = [1,2,3,4,5,6]
    resultados=[random.choice(eventos) for_in range(s)]
print(f"Resultados de {s} lanzamientos de un dado---")
for i, resultado in enumerate(resultados, start=1)
   print(f"Lanzamiento {i}:{resultado}")

   print(f"Lanzamiento {i}: {resultado}")
print("\n---Conteo total---")
for cara in eventos:
    conteo = resultados.count(cara)
    print(f"Cara {cara}:{conteo} veces")
    simular_Lanzamientos(20)
    