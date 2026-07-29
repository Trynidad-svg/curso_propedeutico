mes = input("Ingrese el mes: ").lower()
match mes:
    case "diciembre" | "enero" | "febrero":
        print("Invierno")
    case "marzo" | "abril" | "mayo":
        print("Primavera")
    case "junio" | "julio" | "agosto":
        print("Verano")
    case "septiembre" | "octubre" | "noviembre":
        print("Otoño")
    case _:
        Estacion = "Mes no valido"
print("La estacion del año es:", Estacion)
  