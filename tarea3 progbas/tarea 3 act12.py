import random

numero_secreto = random.randint(1, 100)
adivinanza = None
while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número entre 1 y 100: "))
    if adivinanza < numero_secreto:
        print("El número secreto es mayor.")
    elif adivinanza > numero_secreto:
        print("El número secreto es menor.")

print(f"al fin adivinaste xddd, es: {numero_secreto}")
