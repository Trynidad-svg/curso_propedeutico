pesos = float(input("Ingrese la cantidad de pesos mexicanos: "))

print("Elige la moneda a la que deseas convertir: ")
print("1. Dolar (USD), 2. Euro (EUR), 3. Bath (THB), 4. Yen (JPY), 5. Won (KRW), 6. Dolar Australiano (AUD), 7. Sol (PEN), 8. Dolar Canadiense (CAD), 9. Bolivar (VES), 10. Peso Argentino (ARS)")
opcion = int(input("Ingresa tu opcion: "))   

match opcion:
     case 1:
         dinero_convertido = pesos / 16.5
         moneda = "Dolar (USD)"
     case 2:
         dinero_convertido = pesos / 18.0
         moneda = "Euro (EUR)"
     case 3:
         dinero_convertido = pesos / 0.45
         moneda = "Bath (THB)"
     case 4: 
         dinero_convertido = pesos / 0.12
         moneda = "Yen (JPY)"
     case 5: 
         dinero_convertido = pesos / 0.013
         moneda = "Won (KRW)"
     case 6:
         dinero_convertido = pesos / 11.5
         moneda = "Dolar Australiano (AUD)"
     case 7: 
         dinero_convertido = pesos / 2.8
         moneda = "SOL (PEN)"
     case 8: 
         dinero_convertido = pesos / 8.2
         moneda = "Dolar Canadiense (CAD)"
     case 9:
         dinero_convertido = pesos / 0.0023
         moneda = "Bolivar (VES)"
     case 10:
         dinero_convertido = pesos / 0.046
         moneda = "Peso Argentino (ARS)"
     case _:
         print("Error: Opcion invalida. Por favor, elige un numero del 1 al 10.")
         pesos = None
         dinero_convertido = None
         moneda = None
if pesos is None or dinero_convertido is None or moneda is None:
    # no valid conversion
    pass
else:
    print(f"Tu cantidad de {pesos} pesos mexicanos (MX) convertida a {moneda} es: {dinero_convertido}")


      
      

