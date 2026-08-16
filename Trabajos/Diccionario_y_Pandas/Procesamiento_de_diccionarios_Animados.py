# Procesamiento de diccionarios animados.
Escuela = {
    "A101": {"Nombre": "Ana", "Calificaciones": {"Matematicas": 85, "Fisica": 90, "Programacion": 95}},
3    "A102": {"Nombre": "Luis", "Calificaciones": {"Matematicas": 78, "Fisica": 82, "Programacion": 80}} ,
4    "A103": {"Nombre": "Pedro", "Calificaciones": {"Matematicas": 92, "Fisica": 88, "Programacion": 98}}
}
# Variables
mejor_promedio=-1
nombre_mejor_estudiante=""
suma_programacion=0
total_estudiantes=len(Escuela)

# 1.- Calcule e imprima el promedio individual de cada estudiante.
print("---Promedio individuales de cada estudiante---")
for id_estudiante, info in Escuela.items():
    Calificaciones = info["Calificaciones"].values()
    promedio_individual = sum(Calificaciones) / len(Calificaciones)
    print(f"Estudiante: {info['Nombre']} | Promedio: {promedio_individual:.2f}")

# 2.-Encuentre y muestre el nombre del estudiante con el mejor promedio general.
    if promedio_individual > mejor_promedio:
    mejor_promedio = promedio_individual
    nombre_mejor_estudiante = info["Nombre"]

# 3.- Calcule el promedio general de toda la escuela para la materia de “Programacion”.
    suma_programacion += info["Calificaciones"]["Programacion"]
print("\n" + "-"*40)
print(f"Mejor promedio general: {nombre_mejor_estudiante} (Promedio: {mejor_promedio:.2f})")
promedio_programacion = suma_programacion / total_estudiantes
print(f"Promedio general de Programacion: {promedio_programacion:.2f}")
