precio = float(input("Ingrese el precio de la compra: "))
if precio >= 1000:
    descuento = 0.05
elif precio >= 200:
    descuento = 0.02
elif precio >= 500:
    descuento = 0.03
else:
    descuento = 0.20
precio_final = precio - (precio * descuento)
print("El precio final con descuento es:", precio_final)