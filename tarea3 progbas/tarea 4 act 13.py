nombres_input = input("Ingresa los nombres separados por comas: ")


nombres = nombres_input.split(',')
nombres = [nombre.strip() for nombre in nombres]

nombres_ordenados = sorted(nombres)

print("Los nombres ordenados alfabeticamente son:")
for nombre in nombres_ordenados:
    print(nombre)
