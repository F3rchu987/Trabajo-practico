print("Las opciones para jugar es responder con un (1) para si y (2) para no")
pregunta=int(input("¿Colon descubrió Ámerica?:"))
if pregunta==1:
    pregunta1=int(input("¿La idependencia de colombia fue en el año 1500?:"))
    if pregunta1==2:
         pregunta2=int(input("¿The Doors fue un grupo de rock americano?:"))
         if pregunta2==1:
             pregunta3=int(input("¿Carlos vives interpreta música Clásica?:"))
             if pregunta3==2:
                pregunta4=int(input("¿El creador de linux es Linus Benedict Torvald´s?:"))
                if pregunta4==1:
                   print("Has ganado el juego con todas las respuestas correctas")
                else:
                    print("Error jurgo terminado")
             else:
                 print("Error juego terminado")
         else:
             print("Error juego terminado")
    else:
         print("Error juego terminado")
else:
     print("Error juego terminado")