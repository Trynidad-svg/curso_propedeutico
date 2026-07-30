# Programa para leer 8 números
# y encontrar el máximo y mínimo

numeros = []

for i in range(8):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

# Uso de funciones built-in
max_builtin = max(numeros)
min_builtin = min(numeros)

# Uso de un bucle manual
max_manual = numeros[0]
min_manual = numeros[0]

for numero in numeros[1:]:
    if numero > max_manual:
        max_manual = numero

    if numero < min_manual:
        min_manual = numero

# Mostrar resultados
print("Máximo usando built-in:", max_builtin)
print("Mínimo usando built-in:", min_builtin)
print("Máximo usando bucle manual:", max_manual)
print("Mínimo usando bucle manual:", min_manual)
