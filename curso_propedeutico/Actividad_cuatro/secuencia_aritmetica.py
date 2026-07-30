def generar_sucesion_aritmetica(primer_termino, razon, cantidad):
    return [primer_termino + i * razon for i in range(cantidad)]


def main():
    try:
        primer_termino = float(input("Primer término: "))
        razon = float(input("Razón (diferencia): "))
        cantidad = int(input("Número de términos: "))
    except ValueError:
        print("Entrada inválida. Usa números.")
        return

    if cantidad <= 0:
        print("La cantidad de términos debe ser mayor que 0.")
        return

    sucesion = generar_sucesion_aritmetica(primer_termino, razon, cantidad)
    print("Secuencia aritmética:")
    print(" ".join(str(int(x)) if x.is_integer() else str(x) for x in sucesion))


if __name__ == "__main__":
    main()
