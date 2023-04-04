# Pedir al usuario el nombre y la antiguedad del empleado

nombre = input("Ingrese el nombre del empleado: ")
antiguedad = int(input("Ingrese la antiguedad del empleado (en años): "))

# Calcular el bono para el empleado

if antiguedad >= 5:
    bono = 1000
else:
    bono = 500

# Imprimir el nombre del empleado y su bono

print("El empleado", nombre, "tiene una antiguedad de", antiguedad, "años y recibira un bono de", bono, "dolares.")