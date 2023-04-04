# Lista de empleados

empleados =[("Juan", "M"), ("Maria", "F"),("Pedro", "M"),("Ana","F"),("joaquin","B")]

#Asignar un regalo segun el genero

for empleado in empleados:
    nombre, genero = empleado
    if genero == "M":
        print(nombre, "recibio una corbata como regalo")
    elif genero == "F":
        print(nombre, "Recibio un bolso como regalo") 
    else:
        print(nombre, "Escoge una de ambas opciones de regalo")           
    