precio=int(input("ingrese el precio por litros: "))
pasajeros=int(input("ingrese la cantidad de pasajeros: "))
consumo=int(input("ingrese el cosumo: "))
distancia=int(input("ingrese la distancia: "))

total=precio*consumo*distancia
porpersonas=total/pasajeros

print("costo total de combustible: ",total)
print("cada pasajeros paga: ",porpersonas)