# Ejercicio 7 - Escribir un inventario ordenado


def write_inventory(filename, inventory):
    # 1. Obtenemos las claves del diccionario (los nombres de los ítems)
    # y las ordenamos alfabéticamente usando la función sorted()
    items_ordenados = sorted(inventory.keys())

    # 2. Abrimos el archivo en modo escritura ('w')
    # Esto creará el archivo si no existe, o lo vaciará por completo si ya existía
    with open(filename, 'w') as archivo:
        # 3. Recorremos los ítems ya ordenados
        for item in items_ordenados:
            # Buscamos la cantidad que le corresponde a este ítem
            cantidad = inventory[item]

            # 4. Escribimos en el archivo con el formato exacto 'item:cantidad'
            # Es fundamental agregar el '\n' al final de la cadena
            archivo.write(f"{item}:{cantidad}\n")

    # La función no tiene un 'return', por ende retorna None por defecto