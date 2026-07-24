print("CARTA DEL RESTAURANTE")
print("1-Milanesa con papas-$2500")
print("2-Hamburguesa completa-$2200")
print("3-Pizza individual-$2000")
pedido=int(input("¿Cual de las opciones deseas pedir?:"))
if pedido==1:
    cantidad=int(input("¿Cuantos platos de milanesas con papas deseas?:"))
    total=cantidad*2500
    print("El total del pedido es:", total)
if pedido==2:
   cantidad=int(input("¿Cuantos platos de hamburguesas deseas?:"))
   total=cantidad*2200
   print("El total del pedido es:", total)
elif pedido==3:
    cantidad=int(input("¿Cuantos platos de pizza deseas?:"))
    total=cantidad*2000
    print("El total del pedido es:", total)