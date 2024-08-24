entrada = input("ingresa numeros separados por comas: ")
numeros_cadena = entrada.split(',')

suma = sum(float(numero) for numero in numeros_cadena)
print(f"la suma de los numeros es: {suma}")
