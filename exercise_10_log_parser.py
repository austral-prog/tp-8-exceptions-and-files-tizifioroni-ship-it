# Ejercicio 10 - Parser de archivos de log


def parse_log(filename):
    resultado = {}

    # 1. Abrimos el archivo de forma segura. Si no existe, propaga FileNotFoundError solo.
    with open(filename, 'r') as archivo:
        for linea in archivo:
            # Quitamos los saltos de línea al final para evaluar correctamente el contenido
            linea_cruda = linea.rstrip('\r\n')

            # Las líneas completamente vacías se ignoran y no se consideran inválidas
            if linea_cruda.strip() == "":
                continue

            # 2. Validamos si la línea contiene el carácter ':'
            if ":" not in linea_cruda:
                raise ValueError("invalid log line")

            # 3. Separamos el nivel del mensaje por los dos puntos ':'.
            # Usamos maxsplit=1 por si el mensaje adentro contiene otros dos puntos.
            nivel_sucio, mensaje_sucio = linea_cruda.split(':', 1)

            # 4. Limpiamos los espacios extras al principio y al final de ambos elementos
            nivel = nivel_sucio.strip()
            mensaje = mensaje_sucio.strip()

            # 5. Agrupamos en el diccionario de listas
            if nivel in resultado:
                resultado[nivel].append(mensaje)
            else:
                resultado[nivel] = [mensaje]

    return resultado