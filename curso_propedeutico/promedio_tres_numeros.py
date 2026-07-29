# Programa 2: promedio de tres numeros

def calcular_promedio():
    print("Calcula el promedion de tres numeros")
    try: 
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        num3 = float(input("Ingrese el tercer numero: ")) 

        promedio = (num1 + num2 + num3) / 3

        print(f"\nResultados:")
        print(f"numeros ingresados: {num1}, {num2}, {num3}")
        print(f"El promedio de los tres numeros es: {promedio:.2f}\n")





    except ValueError:
        print("Error: Por favor ingrese valores numericos validos")


if __name__ == "__main__":
    calcular_promedio()

