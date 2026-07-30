# Programa que lee 10 números enteros
numeros = []
pares = 0
impares = 0

for i in range(10):
    n = int(input("Ingrese un número entero: "))
    numeros.append(n)

    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print("La lista ingresada es:", numeros)
print("Números pares:", pares)
print("Números impares:", impares)

# Fin del programa
