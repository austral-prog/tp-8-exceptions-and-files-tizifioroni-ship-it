# Ejercicio 3 - Ventas por producto


def read_sales(filename):
    # Empezamos con el diccionario vacío
    ventas_dict = {}

    # 1. Abrimos el archivo de forma segura
    with open(filename, 'r') as archivo:
        # Leemos todo el contenido junto (ya que está todo en una sola línea)
        contenido = archivo.read().strip()

        # Si el archivo está vacío después del strip, devolvemos el dict vacío
        if not contenido:
            return ventas_dict

        # 2. Separamos las distintas ventas usando el punto y coma ';'
        ventas_individuales = contenido.split(';')

        for venta in ventas_individuales:
            # Validamos por si queda un ';' colgado al final del archivo que genere un string vacío
            if venta != "":
                # 3. Separamos el producto del monto usando los dos puntos ':'
                producto, monto_str = venta.split(':')

                # Convertimos el monto a número flotante (float)
                monto = float(monto_str)

                # 4. Agrupamos en el diccionario creando o añadiendo a la lista
                if producto in ventas_dict:
                    ventas_dict[producto].append(monto)
                else:
                    ventas_dict[producto] = [monto]

    return ventas_dict


def process_sales(data):
    # Recorremos el diccionario en su orden natural
    for producto, lista_montos in data.items():
        # Calculamos los totales usando las funciones matemáticas básicas
        total = sum(lista_montos)
        promedio = total / len(lista_montos)

        # Imprimimos usando f-strings controlando que muestre exactamente 2 decimales (: .2f)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")