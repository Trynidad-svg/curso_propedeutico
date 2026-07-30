import math


def mcd_euclides_iterativo(a: int, b: int) -> int:
    """Calcula el máximo común divisor usando el algoritmo de Euclides de forma iterativa."""
    a = abs(a)
    b = abs(b)

    if a == 0 and b == 0:
        return 0

    while b != 0:
        a, b = b, a % b

    return a


numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

mcd_personal = mcd_euclides_iterativo(numero1, numero2)
mcd_math = math.gcd(abs(numero1), abs(numero2))

print(f"MCD con función propia: {mcd_personal}")
print(f"MCD con math.gcd: {mcd_math}")

if mcd_personal == mcd_math:
    print("La verificación fue correcta.")
else:
    print("Hay una discrepancia entre los resultados.")
