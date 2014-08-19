    #Importamos opcion de aleatorio
import random
    #Guardamos valor aleatorio
opcionMaquina = random.randrange(0,3)

#Converetimos el rango aleatorio en string segun su valor
if opcionMaquina == 0:
	opcionMaquina = "piedra"
elif opcionMaquina == 1:
	opcionMaquina = "papel"
elif	opcionMaquina == 2:
	opcionMaquina = "tijeras"	

    #Funcion cuando el usuario elije piedra
def piedra():
	print "La maquina elijio::"+opcionMaquina
	if opcionMaquina == "piedra": 
		print "Esto es un empate"
	elif opcionMaquina == "papel":
		print "Maquina Gana"
	elif opcionMaquina == "tijeras": 
		print "Tu ganas"

	#Funcion cuando el usuario elije papel	
def papel():
	print "La maquina elijio::"+opcionMaquina
	if opcionMaquina == "piedra": 
		print "Tu ganas"
	elif opcionMaquina == "papel":
		print "Esto es un empate"
	elif opcionMaquina == "tijeras": 
		print "Maquina Gana"
		
	#Funcion cuando el usuario elije tijeras	
def tijeras():
	print "La maquina elijio::"+opcionMaquina
	if opcionMaquina == "piedra": 
		print "Maquina Gana"
	elif opcionMaquina == "papel":
		print "Tu Ganas"
	elif opcionMaquina == "tijeras": 
		print "Esto es un empate"