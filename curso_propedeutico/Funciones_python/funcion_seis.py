import math


def raiz_newton(numero, tolerancia=1e-10, max_iter=100):
    if numero < 0:
        raise ValueError("No existe raíz cuadrada real para números negativos.")
    if numero == 0:
        return 0.0
    x = numero / 2.0
    for _ in range(max_iter):
        xn = 0.5 * (x + numero / x)
        if abs(xn - x) < tolerancia:
            return xn
        x = xn
    return x


numero = 16
resultado = raiz_newton(numero)
print(f"Newton-Raphson: {resultado}")
print(f"math.sqrt: {math.sqrt(numero)}")
print(f"Diferencia: {resultado - math.sqrt(numero)}")
