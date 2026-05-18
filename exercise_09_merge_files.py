# Ejercicio 9 - Combinar dos archivos


def merge_files(file1, file2, output):
    # 1. Leemos el contenido del primer archivo
    # Si no existe, Python frena acá lanzando FileNotFoundError
    with open(file1, 'r') as f1:
        contenido1 = f1.read()

    # 2. Leemos el contenido del segundo archivo
    # Si este no existe, también frena acá sin haber tocado el archivo output
    with open(file2, 'r') as f2:
        contenido2 = f2.read()

    # 3. Recién cuando sabemos que ambos textos existen en memoria,
    # abrimos el archivo de salida en modo escritura ('w') para concatenarlos
    with open(output, 'w') as out:
        out.write(contenido1)
        out.write(contenido2)

    # La función no retorna nada (None)