# Ejercicio 6 - Estadísticas de notas por estudiante


def grades_stats(filename):
    resultado = {}

    # 1. Abrimos el archivo de forma segura. Si no existe, lanza FileNotFoundError
    with open(filename, 'r') as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()

            # Si la línea está vacía, se ignora por completo
            if linea_limpia == "":
                continue

            # 2. Separamos el nombre del estudiante de su cadena de notas
            estudiante, notas_juntas = linea_limpia.split(':')

            # 3. Separamos las notas individuales por su coma
            lista_notas_str = notas_juntas.split(',')

            # 4. Convertimos toda la lista de textos a números flotantes (float)
            notas_num = []
            for nota_str in lista_notas_str:
                notas_num.append(float(nota_str))

            # 5. Realizamos los cálculos estadísticos requeridos
            promedio = sum(notas_num) / len(notas_num)
            maximo = max(notas_num)
            minimo = min(notas_num)

            # 6. Guardamos en el diccionario asociando el nombre con la tupla de floats
            resultado[estudiante] = (promedio, maximo, minimo)

    return resultado