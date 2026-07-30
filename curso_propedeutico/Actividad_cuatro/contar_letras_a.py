def contar_letras_a(texto):
    """Cuenta las letras 'a' y 'A' en el texto dado."""
    return texto.count('a') + texto.count('A')

if __name__ == '__main__':
    texto = input('Ingrese un texto: ')
    cantidad = contar_letras_a(texto)
    print(f"Cantidad de letras 'a' o 'A': {cantidad}")
