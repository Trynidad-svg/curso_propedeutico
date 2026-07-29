# Programa 3: Calcular salario neto

salario_bruto = float(input("Salario bruto: "))
porcentaje = float(input("% impuestos: "))
impuesto = salario_bruto * (porcentaje / 100)
deducciones = salario_bruto * (porcentaje / 100)
salario_neto = salario_bruto - impuesto - deducciones
print("Salario neto: ", salario_neto)
