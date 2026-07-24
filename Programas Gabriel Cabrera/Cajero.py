saldo=float(input("Ingrese el saldo disponible:"))
print("1-Retiro")
print("2-Consultar el saldo")
print("3-Depósitar")
opcion=int(input("Elija una de las opciones anteriores:"))
if opcion==1:
    retiro=float(input("Cuanto deseas retirar:"))
    total=saldo-retiro
    print("Se retiraron ", "$",retiro)
    print("Tu saldo actual es de", " $",total)
elif opcion==2:
    print("Tu saldo actual es de", " $",saldo)
if opcion==3:
    deposito=float(input("Cuanto deseas depositar:"))
    total2=saldo+deposito
    print("Se depositaron ", "$",deposito)
    print("Tu saldo actual es de", " $",total2)