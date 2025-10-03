 #Este programa calcula la ley de Ohm
print("ley de ohm")
print("selecciona la opcion")
opcion=int(input("1=voltaje, 2=corriente, 3=resistencia: "))
#calculo según la opción
try:
	if opcion==1:
		#calcular voltaje
		corriente=float(input("corriente (A): "))
		resistencia=float(input("resistencia (Ohm): "))
		voltaje=corriente*resistencia
		print("voltaje=", voltaje, "V")
	elif opcion==2:
		#calcular corriente
		voltaje=float(input("voltaje (V): "))
		resistencia=float(input("resistencia (Ohm): "))
		corriente=voltaje/resistencia
		print("corriente=", corriente, "A")
	elif opcion==3:
		#calcular resistencia
		voltaje=float(input("voltaje (V): "))
		corriente=float(input("corriente (A): "))
		resistencia=voltaje/corriente
		print("resistencia=", resistencia, "Ohm")
	else:
		print("opción inválida")
except Exception as e:
	print("Error en los datos:", e)