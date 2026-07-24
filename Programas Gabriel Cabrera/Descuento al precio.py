precio=int(input("Ingrese el precio del producto:"))
print("1-30%")
print("2-20%")
print("3-5%")
opcion=int(input("Eliga la opción de descuento que deseas realizar:"))
if opcion==1:
    descuento=precio*(30/100)
    preciofinal=precio-descuento
    print("El descuento es de:", preciofinal)
if  opcion==2:
    descuento1=precio*(20/100)
    preciofinal1=precio-descuento1
    print("El descuento es de:", preciofinal1)
if opcion==3:
    descuento2=precio*(5/100)
    preciofinal2=precio-descuento2
    print("El descuento es de:", preciofinal2)