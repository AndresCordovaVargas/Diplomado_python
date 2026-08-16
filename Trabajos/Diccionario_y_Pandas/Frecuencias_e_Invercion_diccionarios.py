import string
texto = "No hay nada noble en ser superior a otra persona; la verdadera nobleza radica en ser superior a tu antiguo yo."
texto_limpio = texto.lower()
for signo in string.puntuacion:
    texto_limpio = texto_limpio.replace(signo, "")
palabras = texto_limpio.split()
frecuencias ={}
for palabra in palabras:
    if palabra in frecuencias:
    frecuencias[palabra] += 1
    else:
    frecuencias[palabra] = 1
print("1. Diccionario de frecuencias:")
print(frecuencias)
print("-" * 50)

diccionario_invertido ={}
for palabra, frec in frecuencias.items():
    if frec not in diccionario_invertido:
        diccionario_invertido[frec] = []
    diccionario_invertido[frec].append(palabra)

print("2. Diccionario invertido (frecuencia -> Palabras):")
print(diccionario_invertido)
print("-" * 50)

palabras_ordenadas = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
print("3. Palabras mas freacuentes:")
for i, elemento in enumerate(palabras_ordenadas[:3]):
    palabra = elemento[0]
    frec = elemento[1]
    print(f"{i+1}. {palabra} con {frec} apariciones.")
