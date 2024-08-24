calificaciones_input = input("Ingresa las calificaciones separadas por comas: ")
calificaciones_cadena = calificaciones_input.split(',')
calificaciones = [float(calificacion) for calificacion in calificaciones_cadena]
promedio = sum(calificaciones) / len(calificaciones)

print(f"El promedio de las calificaciones es: {promedio:.2f}")
