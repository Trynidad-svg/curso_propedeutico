def main():
    try:
        limite = int(input("Ingrese un número límite: ").strip())
    except ValueError:
        print("Entrada inválida.")
        return

    multiplos = [i for i in range(1, limite + 1) if i % 3 == 0 or i % 5 == 0]

    if multiplos:
        print(f"Múltiplos de 3 o 5 hasta {limite}:")
        print(" ".join(str(x) for x in multiplos))
    else:
        print(f"No hay múltiplos de 3 o 5 hasta {limite}.")


if __name__ == "__main__":
    main()
