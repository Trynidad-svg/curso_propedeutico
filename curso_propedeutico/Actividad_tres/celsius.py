celsius = float(input("Ingrese la temperatura en celsius: "))
opcion = input("Convertir a Fahrenheit (F) o Kevin (K): ").upper()
match opcion:
    case "F":
        fahrenheit = (celsius * 9/5) + 32
        print("La temperatura en Fahrenheit es:", fahrenheit)
    case "K":
        kelvin = celsius + 273.15
        print("La temperatura en Kevin es:", kelvin)
    case _:
        print("Opción no válida")