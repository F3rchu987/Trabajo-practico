precio=int(input("ingrese precio del combustible: "))
personas=int(input("ingrese cantidad de personas: "))
consumo=int(input("ingrese el consumo: "))
distancia=int(input("ingrese la distancia: "))
porcentaje=int(input("ingrese el porcentaje: "))

litros= consumo*distancia
costos= litros*precio
ganancia=costos*(porcentaje/100)
presiofinal=costos+ganancia
porpasajero=presiofinal/ personas

print("costo total del combustible es: ",costos )
print("el valor del pasajero es: ", porpasajero )
print("presio finales: ",presiofinal )