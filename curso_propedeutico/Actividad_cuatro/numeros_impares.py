def contar_impares(numeros):
    return sum(1 for n in numeros if n % 2 != 0)

if __name__ == "__main__":
    entrada = input("Ingrese números separados por espacios: ")
    try:
        lista = [int(x) for x in entrada.split()]
    except ValueError:
        print("Entrada inválida. Ingrese solo números enteros.")
    else:
        cantidad = contar_impares(lista)
        print(f"Cantidad de números impares: {cantidad}")
