# Ejercicio 4 - Promedio seguro con manejo de errores


def safe_average(filename):
    # Usamos acumuladores para la suma y para contar cuántos números válidos encontramos
    suma_total = 0.0
    contador_validos = 0

    # 1. Abrimos el archivo. Si no existe, propaga FileNotFoundError automáticamente
    with open(filename, 'r') as archivo:
        for linea in archivo:
            # Limpiamos espacios y saltos de línea molestos
            linea_limpia = linea.strip()

            # Si la línea está vacía (por ejemplo, un renglón en blanco al final), la salteamos
            if linea_limpia == "":
                continue

            # 2. Intentamos convertir la línea a flotante
            try:
                numero = float(linea_limpia)
                # Si la conversión tiene éxito, acumulamos
                suma_total = suma_total + numero
                contador_validos = contador_validos + 1
            except ValueError:
                # Si falla (ej: es un texto), el try se interrumpe y cae acá.
                # Al poner 'pass', simplemente ignoramos el error y el bucle sigue con la otra línea.
                pass

    # 3. Validaciones finales después de cerrar el archivo
    # Si el archivo existía pero no contenía ningún número válido
    if contador_validos == 0:
        raise ValueError("no valid numbers")

    # 4. Si todo salió bien, calculamos y retornamos el promedio
    return suma_total / contador_validos