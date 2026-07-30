def invertir_lista(lista):
    invertida = []
    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])
    return invertida

numeros = []

for i in range(6):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

lista_invertida = invertir_lista(numeros)

print("Lista original:", numeros)
print("Lista invertida:", lista_invertida)
