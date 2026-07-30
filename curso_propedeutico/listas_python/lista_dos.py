numeros = []
for i in range(5):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

suma_bucle = 0
for numero in numeros:
    suma_bucle += numero

suma_funcion = sum(numeros)

print("Lista:", numeros)
print("Suma con bucle:", suma_bucle)
print("Suma con sum():", suma_funcion)
