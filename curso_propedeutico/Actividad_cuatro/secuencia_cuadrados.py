def generar_secuencia_cuadrados(n):
    """Devuelve una lista con los primeros n cuadrados naturales."""
    return [i * i for i in range(1, n + 1)]


def main():
    try:
        cantidad = int(input("Ingrese la cantidad de cuadrados a generar: "))
        if cantidad <= 0:
            print("Ingrese un número entero positivo.")
            return
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")
        return

    cuadrados = generar_secuencia_cuadrados(cantidad)
    for indice, valor in enumerate(cuadrados, start=1):
        print(f"{indice}^2 = {valor}")


if __name__ == "__main__":
    main()
