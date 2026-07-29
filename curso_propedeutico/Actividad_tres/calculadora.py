# Calculadora de nota final con validación de rango

parcial = float(input("Nota de parciales (0-100): "))
proyectos = float(input("Nota de proyecto (0-100): "))
examen = float(input("Nota de examen (0-100): "))

nota_final = (parcial * 0.4) + (proyectos * 0.3) + (examen * 0.3)

if(parcial < 0 or parcial > 100) or (proyectos < 0 or proyectos > 100) or (examen < 0 or examen > 100):
   print("Error: las notas deben estar entre 0 y 100")
else: 
    print ("La nota final del estudiante es: ", nota_final)
