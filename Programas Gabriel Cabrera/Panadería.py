print("MENÚ DEL DÍA")
print("1-Pan $1.800 KG")
print("2-Medialunas $600 C/U")
print("3-tortitas $300 C/U")
print("4-Tarta de Chocolate $4.000")
producto=int(input("¿Que deseas llevar:"))
cantidad=float(input("Cuantas unidades deseas llevar:"))
descuento=int(input("¿Que descuento deseas hacer 1(15%)- 2(5%):"))
if producto==1:
    if descuento==1:
        suma=cantidad*1800
        total=suma*0.15
        subtotal=suma-total
        print("El precio final es de: $ ", subtotal)
    if descuento==2:
        suma1_5=cantidad*1800
        total1_5=suma1_5*0.05
        subtotal1_5=suma1_5-total1_5
        print("El precio final es de: $ ", subtotal1_5)
elif producto==2:
    if descuento==1:
        suma2=cantidad*600
        total2=suma2*0.15
        subtotal2=suma2-total2
        print("El precio final es de: $ ", subtotal2)
    if descuento==2:
        suma2_5=cantidad*600
        total2_5=suma2_5*0.05
        subtotal2_5=suma2_5-total2_5
        print("El precio final es de: $ ", subtotal2_5)
if producto==3:
    if descuento==1:
        suma3=cantidad*300
        total3=suma3*0.15
        subtotal3=suma3-total3
        print("El precio final es de: $ ", subtotal3)
    if descuento==2:
        suma3_5=cantidad*300
        total3_5=suma3_5*0.05
        subtotal3_5=suma3_5-total3_5
        print("El precio final es de: $ ", subtotal3_5)
elif producto==4:
    if descuento==1:
        suma4=cantidad*4000
        total4=suma4*0.15
        subtotal4=suma4-total4
        print("El precio final es de: $ ", subtotal4)
    if descuento==2:
        suma4_5=cantidad*4000
        total4_5=suma4_5*0.05
        subtotal4_5=suma4_5-total4_5
        print("El precio final es de: $ ", subtotal4_5)