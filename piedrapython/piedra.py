#Piedra papel o tijeras.
#V0.1 BY Abdiel Carrasco.   

    #importamos opciones donde redisen las funciones
import opciones
    #Preguntamos al usuario que opcion desea elegir
opcionUsuario = raw_input("Escoje>>>>> piedra  papel  tijeras--->:")
print "escojiste la opcion::"+opcionUsuario
    #Estructura de control que maneja las funciones a ejecutar.
if opcionUsuario == "piedra":
	opciones.piedra()
elif opcionUsuario == "papel":	
	opciones.papel()
elif opcionUsuario == "tijeras":	
	opciones.tijeras()
else:
	print "Que pasa aca esta no es una opcion valida !!Intentalo de nuevo!!"	




