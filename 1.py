#pedir al usuario que ingrese su peso en kilogramos y su altura en mm

peso =float(input("Ingresa tu peso en kilogramos: "))
altura =float(input("Ingresa tu altura en metros: "))

# Calcular el IMC

imc = peso / (altura ** 2)

#Mostrar el resultado al usuario

print("Tu indice de masa corporal (IMC) es:", (imc))