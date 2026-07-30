def es_vocal(caracter):
    """Devuelve True si el carácter es una vocal en español."""
    return caracter.lower() in 'aeiouáéíóúü'


def clasificar_caracter(caracter):
    if len(caracter) != 1:
        return 'Ingrese un solo carácter.'
    if not caracter.isalpha():
        return 'No es una letra.'
    if es_vocal(caracter):
        return 'Vocal'
    return 'No vocal'


def main():
    entrada = input('Ingrese una letra: ').strip()
    resultado = clasificar_caracter(entrada)
    print(resultado)


if __name__ == '__main__':
    main()
