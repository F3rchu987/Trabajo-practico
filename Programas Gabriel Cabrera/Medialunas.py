print("ATENCIÓN NO INGRESAR MENOS DE 100 unidades")
cantidad=int(input("¿Cuantas docenas deseas hacer?:"))
harina=500*2
leche=225 * 2
levadura=25 * 2
huevo=1*2
azucar=100 *2 
miel= 15 *2
sal=15 *2
manteca=200 * 2
harina_empaste= 25*2
print("Las cantidad que necesitas son las siguientes")
print("Harina:", (harina*cantidad)/1000, "KG")
print("Leche:", (leche*cantidad)/1000, "LTS")
print("Levadura:", (levadura*cantidad)/1000, "KG")
print("Huevo:", huevo, "UNIDAD")
print("Azucar:", (azucar*cantidad)/1000, "KG")
print("Miel:", (miel*cantidad)/1000, "KG")
print("Sal:", (sal*cantidad)/1000, "KG")
print("Manteca:", (manteca*cantidad)/1000, "KG")
print("Harina para empaste:", (harina_empaste*cantidad)/1000, "KG")