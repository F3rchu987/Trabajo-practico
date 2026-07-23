precio=int(input("Ingrese el precio del combustible por litro:"))
pasajero=int(input("Ingrese la cantidad de pasajeros:"))
consumo=int(input("Ingrese el consumo del vehículo (lts/km):"))
distancia=int(input("Ingrese la distancia del viaje (km):"))
costototal=consumo*distancia*precio
costoxpersona=costototal/pasajero
print("El costo total del combustible es: ", costototal)
print("Cada pasajero debe pagar: ", costoxpersona)