# Ejercicio 2 - Contar palabras en un archivo


def count_words(filename):
    # Inicializamos el diccionario vacío donde acumularemos los conteos
    frecuencias = {}

    # 1. Abrimos el archivo. Si no existe, lanzará FileNotFoundError automáticamente
    with open(filename, 'r') as archivo:

        # 2. Leemos el archivo línea por línea
        for linea in archivo:
            # 3. Convertimos toda la línea a minúsculas para no distinguir mayúsculas
            linea_minuscula = linea.lower()

            # 4. Dividimos la línea en palabras usando los espacios como corte
            # .split() elimina automáticamente los saltos de línea (\n) y espacios extras
            palabras = linea_minuscula.split()

            # 5. Recorremos cada palabra de la línea actual
            for palabra in palabras:
                # Si la palabra ya está en el diccionario, sumamos 1
                if palabra in frecuencias:
                    frecuencias[palabra] = frecuencias[palabra] + 1
                # Si es la primera vez que aparece, la inicializamos en 1
                else:
                    frecuencias[palabra] = 1

    # 6. Retornamos el diccionario con los resultados finales
    return frecuencias
