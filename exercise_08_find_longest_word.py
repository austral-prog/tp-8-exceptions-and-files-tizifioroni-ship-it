# Ejercicio 8 - Palabra más larga de un archivo


def find_longest_word(filename):
    palabra_mas_larga = ""
    encontro_palabras = False

    # 1. Abrimos el archivo. Si no existe, propaga FileNotFoundError automáticamente
    with open(filename, 'r') as archivo:
        for linea in archivo:
            # 2. Dividimos la línea en palabras usando .split()
            # Esto remueve automáticamente espacios múltiples y saltos de línea (\n)
            palabras = linea.split()

            for palabra in palabras:
                # Marcamos que al menos encontramos una palabra válida en el archivo
                encontro_palabras = True

                # 3. Comparamos longitudes. Usamos '>' (estricto) para que,
                # en caso de empate, se quede con la primera que apareció.
                if len(palabra) > len(palabra_mas_larga):
                    palabra_mas_larga = palabra

    # 4. Si terminó el archivo y nunca procesamos ninguna palabra, lanzamos el error
    if not encontro_palabras:
        raise ValueError("file has no words")

    return palabra_mas_larga