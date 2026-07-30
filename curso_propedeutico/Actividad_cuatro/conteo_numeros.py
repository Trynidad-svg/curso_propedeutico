def main():
    entrada = input("Ingrese números separados por espacios: ").strip()
    if not entrada:
        print("No se ingresaron números.")
        return

    try:
        numeros = [float(valor) for valor in entrada.split()]
    except ValueError:
        print("Entrada inválida. Ingrese solo números.")
        return

    print(f"Cantidad de números: {len(numeros)}")

if __name__ == "__main__":
    main()
