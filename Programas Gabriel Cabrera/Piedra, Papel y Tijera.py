import random
computadora = random.randint(1, 3)
print("Juego de Piedra, Papel y Tijera")
print("Opción 1- Piedra")
print("Opción 2- Papel")
print("Opción 3- Tijera")
usuario=int(input("Elija una de las opciones para empezar el juego: "))
print("La computadora eligio el N°:", computadora)
if (usuario==1 and computadora==1)or (usuario==2 and computadora==2) or (usuario==3 and computadora==3):
    print("Empate")
elif (usuario==1 and computadora==3) or (usuario==2 and computadora==1) or (usuario==3 and computadora==2):
    print("Ganó el usuario")
if (usuario==1 and computadora==2) or (usuario==2 and computadora==3) or (usuario==3 and computadora==1):
    print("Ganó la computadora")