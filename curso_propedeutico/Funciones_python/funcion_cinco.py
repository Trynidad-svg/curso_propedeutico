cadena = input("Ingrese una cadena: ")
caracter_antiguo = input("Ingrese el carácter a reemplazar: ")
caracter_nuevo = input("Ingrese el carácter nuevo: ")

resultado_replace = cadena.replace(caracter_antiguo, caracter_nuevo)


def reemplazo_manual(cadena, caracter_antiguo, caracter_nuevo):
    contador = 0
    nueva_cadena = []

    for caracter in cadena:
        if caracter == caracter_antiguo:
            nueva_cadena.append(caracter_nuevo)
            contador += 1
        else:
            nueva_cadena.append(caracter)

    return "".join(nueva_cadena), contador


resultado_manual, cantidad_reemplazos = reemplazo_manual(
    cadena, caracter_antiguo, caracter_nuevo
)

print("Resultado con replace():", resultado_replace)
print("Resultado con función manual:", resultado_manual)
print("Número de reemplazos:", cantidad_reemplazos)
