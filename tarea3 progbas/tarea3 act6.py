nombre_archivo = input("Ingresa el nombre del archivo de texto (incluye la extensión .txt): ")
try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
    print("\nContenido del archivo:")
    print(contenido)

except FileNotFoundError:
    print("El archivo no se encontro, Asegurate de que el nombre y la ruta sean correctos")
