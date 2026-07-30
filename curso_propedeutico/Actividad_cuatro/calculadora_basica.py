def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

def calculadora():
    print("=== CALCULADORA BÁSICA ===")
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    while True:
        opcion = input("\nIngresa tu opción (1/2/3/4/5): ")
        
        if opcion == "5":
            print("¡Hasta luego!")
            break
        
        if opcion in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                
                if opcion == "1":
                    print(f"Resultado: {num1} + {num2} = {suma(num1, num2)}")
                elif opcion == "2":
                    print(f"Resultado: {num1} - {num2} = {resta(num1, num2)}")
                elif opcion == "3":
                    print(f"Resultado: {num1} × {num2} = {multiplicacion(num1, num2)}")
                elif opcion == "4":
                    resultado = division(num1, num2)
                    print(f"Resultado: {num1} ÷ {num2} = {resultado}")
            except ValueError:
                print("Error: Por favor ingresa números válidos")
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    calculadora()
