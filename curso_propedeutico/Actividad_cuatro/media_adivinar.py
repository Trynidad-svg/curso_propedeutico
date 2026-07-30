def main():
    print("Calcular la media de números positivos")
    positivos = []

    while True:
        entrada = input("Ingrese un número (o presione Enter para terminar): ").strip()
        if entrada == "":
            break

        try:
            valor = float(entrada)
        except ValueError:
            print("Valor no válido. Intente de nuevo.")
            continue

        if valor > 0:
            positivos.append(valor)

    if positivos:
        media = sum(positivos) / len(positivos)
        print(f"Media de los {len(positivos)} números positivos: {media}")
    else:
        print("No se ingresaron números positivos.")


if __name__ == "__main__":
    main()
