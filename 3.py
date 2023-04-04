# Pedir al usuario el nombre del empleado
nombre =input("Ingrese el nombre del empleado: ")

#Pedir al usurio la cantidad de horas trabajadas 
horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))

# Pedir al usuario el valor de la hora trabajada

valor_hora = float(input("Ingrese el valor de la hora trabajada: "))

# Calcular el valor total

valor_total = horas_trabajadas * valor_hora

# Imprimir resultados

print("El empleado", nombre, "trabajo", horas_trabajadas, "horas a un valor de", valor_hora, "por hora.")
print("El valor total de las horas trabajadas es:", valor_total)
