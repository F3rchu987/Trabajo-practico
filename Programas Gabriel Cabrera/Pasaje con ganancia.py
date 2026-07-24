precio=int(input("Ingrese el precio del combustible por litro:"))
pasajero=int(input("Ingrese la cantidad de pasajeros:"))
consumo=int(input("Ingrese el consumo del vehículo (lts/km):"))
distancia=int(input("Ingrese la distancia del viaje (km):"))
porcentaje=int(input("Ingrese el porcentaje que deseas ganas:"))
litros=consumo*distancia
costocombustible=litros*precio
ganancia=costocombustible*(porcentaje/100)
total=costocombustible+ganancia
precioxpasajero=total/pasajero
print("El valor por pasajero es de: ", precioxpasajero)
print("El costo del combustible es de: ", costocombustible)
print("el precio final es de: ", total)
