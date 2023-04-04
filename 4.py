import datetime

# Pedir al usuario su fecha de nacimiento

fecha_nacimiento = input("Ingrese su fecha de nacimiento en el formato AAAA-MM-DD: ")

# Obtener la fecha actual
fecha_actual = str(datetime.date.today())

# separar el año, mes y dia de la fecha de nacimiento ya la fecha actual
anio_nacimiento, mes_nacimiento, dia_nacimiento =map(int, fecha_nacimiento.split("-"))
anio_actual, mes_actual, dia_actual = map(int,fecha_actual.split("-"))


#calcular la edad

edad = anio_actual - anio_nacimiento - ((mes_actual, dia_actual) < (mes_nacimiento, dia_nacimiento))

#imprimir la edad

print("Tu edad es:",edad)