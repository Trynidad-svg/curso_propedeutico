import random

def jugar_adivinar_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("Adivina el número entre 1 y 100.")

    while True:
        try:
            apuesta = int(input("Ingresa tu suposición: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        intentos += 1

        if apuesta < numero_secreto:
            print("Demasiado bajo.")
        elif apuesta > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
            break

if __name__ == "__main__":
    jugar_adivinar_numero()
