# Ejercicio 5 - CSV a lista de diccionarios


def csv_to_dict(filename):
    resultado = []

    # 1. Abrimos el archivo de manera segura
    with open(filename, 'r') as archivo:
        # Leemos todas las líneas del archivo en una lista
        lineas = archivo.readlines()

        # Si el archivo está vacío o solo tiene el header, retornamos []
        if len(lineas) <= 1:
            return resultado

        # 2. La primera línea es el encabezado.
        # La limpiamos y la separamos por comas para tener las llaves: ['name', 'age', 'city']
        header = lineas[0].strip().split(',')

        # 3. Recorremos las líneas de datos (empezando desde la posición 1 en adelante)
        for linea in lineas[1:]:
            linea_limpia = linea.strip()

            # Saltamos renglones vacíos si los hubiera
            if linea_limpia == "":
                continue

            # Separamos los valores de la fila por su coma
            valores = linea_limpia.split(',')

            # 4. Construimos el diccionario para esta fila mapeando con el header
            # Convertimos la edad (posición 1) a entero 'int' como pide la consigna
            persona_dict = {
                header[0]: valores[0],  # 'name': string
                header[1]: int(valores[1]),  # 'age': entero (int)
                header[2]: valores[2]  # 'city': string
            }

            # Agregamos el diccionario de la fila a nuestra lista final
            resultado.append(persona_dict)

    return resultado
