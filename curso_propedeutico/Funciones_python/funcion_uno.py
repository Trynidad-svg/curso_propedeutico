import math


def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limite = math.isqrt(n)
    divisor = 3
    while divisor <= limite:
        if n % divisor == 0:
            return False
        divisor += 2

    return True


try:
    numero = int(input("Ingrese un número entero: "))
    if es_primo(numero):
        print(f"{numero} es primo.")
    else:
        print(f"{numero} no es primo.")
except ValueError:
    print("Error: debe ingresar un número entero válido.")
