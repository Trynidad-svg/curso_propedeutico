def es_palindromo(cadena):
    cadena = cadena.lower()
    cadena_sin_espacios = ''.join(cadena.split())
    return cadena_sin_espacios == cadena_sin_espacios[::-1]


frase = input("Ingrese una frase: ")
resultado = es_palindromo(frase)
frase_limpia = ''.join(frase.lower().split())

if resultado:
    print("La frase es palíndromo.")
else:
    print("La frase no es palíndromo.")

print(f"Longitud de la cadena limpia: {len(frase_limpia)}")
