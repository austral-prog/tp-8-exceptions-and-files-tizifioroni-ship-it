# Ejercicio 1 - Leer líneas de un archivo


def read_lines(filename):
    resultado = []

    # 1. Abrimos el archivo en modo lectura ('r')
    with open(filename, 'r') as archivo:

        # 2. Recorremos el archivo línea por línea
        for linea in archivo:
            # 3. Limpiamos espacios
            linea_limpia = linea.strip()

            # 4. Validamos que no esté en blanco
            if linea_limpia != "":
                resultado.append(linea_limpia)

    # 5. Retornamos la lista final
    return resultado