print("PIDRA PAPEL O TIJERA ")



print("USUARIO")
print("1-PIEDRA ")
print("2-PAPEL")
print("3-TIJERA")
print("4-SALIR")
player=input(": ")




print("COMPUTADORA ")
print("1-PIEDRA ")
print("2-PAPEL")
print("3-TIJERA")
print("4-SALIR")
print("La computadora eligio: ", computadora )

if (player == 1 and  computadora == 1):
    print("empate ")
    
elif (player == 1 and  computadora == 3):
    print("ganaste ")
    
elif (player == 2 and  computadora == 1):
    print("ganaste ")
    
elif (player == 3 and  computadora == 2):
    print("ganaste ")


else :
    print("perdiste ")




