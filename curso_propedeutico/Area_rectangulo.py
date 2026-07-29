# Programa 1: area de un rectangulo
def calcular_area_rectangulo():
    print("calcula el area del rectangulo")
    try:
        base = float(input("Ingrese la base del rectangulo:"))
        altura = float(input("Ingrese la altura del rectangulo:"))



        area = base * altura

        print(f"\nResultados:")
        print(f"Base ingresada: {base}")
        print(f"Altura ingresada: {altura}")
        print(f"Area del rectangulo: {area}")



        print(f"El area del rectangulo es: {area}")
    except ValueError:
        print("Error: Ingrese valores numericos validos")

if __name__ == "__main__":
    calcular_area_rectangulo()
