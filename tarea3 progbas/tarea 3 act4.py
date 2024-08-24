from datetime import datetime
fecha_nacimiento = input("Ingresa tu fecha de nacimiento (YYYY-MM-DD): ")
fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
fecha_actual = datetime.now()
dias_pasados = (fecha_actual - fecha_nacimiento).days

print(f"Han pasado {dias_pasados} días desde que naciste")
