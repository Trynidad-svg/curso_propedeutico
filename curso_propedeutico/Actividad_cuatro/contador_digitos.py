def contar_digitos(numero):
    """Retorna la cantidad de dígitos en un número entero."""
    numero = str(abs(int(numero)))
    return len(numero)


if __name__ == "__main__":
    entrada = input("Ingrese un número: ").strip()
    try:
        cantidad = contar_digitos(entrada)
        print(cantidad)
    except ValueError:
        print("Entrada inválida")
