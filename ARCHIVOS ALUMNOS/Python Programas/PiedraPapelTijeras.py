import random

while True:
    print(" /------------------------------------\\")
    print("|       ¡Piedra papel o tijeras!       |")
    print("|______________________________________|")
    print("|            Elegí una opción          |")
    print("|               1 Piedra               |")
    print("|               2 Papel                |")
    print("|               3 Tijeras              |")
    print(" \\_____________________________________/")


    jugador = int(input())


    computadora = random.randint(1,3)


    if computadora == 1:
        eleccion_compu = "Piedra"

    if computadora == 2:
        eleccion_compu = "Papel"

    if computadora == 3:
        eleccion_compu = "Tijeras"


    print("La computadora eligió:", eleccion_compu)

    if jugador == computadora:
        print("Empate")

    if jugador == 1:
        if computadora == 2:
            print("Gana la computadora, suerte la proxima")
        if computadora == 3:
            print("¡Ganaste!")

    if jugador == 2:
        if computadora == 1:
            print("¡Ganaste!")
        if computadora == 3:
            print("Gana la computadora, suerte la proxima")

    if jugador == 3:
        if computadora == 1:
            print("Gana la computadora, suerte la proxima")
        if computadora == 2:
            print("¡Ganaste!")

    if jugador < 1:
        print("Error opcion no valida")

    if jugador > 3:
        print("Error, opcion no valida")

    if input("¿Otra vez? 1=si, 2=no: ") != "1":
        break