producto=int(input("ingrese el precio del producto"))
print("ahora eliga un descucento : ") 
print("1-30%")
print("2-20%")
print("3- 5%")

num1=int(input(": "))



if ( num1 == 1 ):
    
    descuento=producto*0.3
    presiofinal=producto-descuento
    
    print("precio del producto es :$ ",presiofinal)
    
elif (num1 == 2 ):
    
        
    descuento=producto*0.2
    presiofinal=producto-descuento
    
    print("precio del producto es :$ ",presiofinal)
    
elif (num1 == 3):
    
        
    descuento=producto*0.05
    presiofinal=producto-descuento
    
    print("precio del producto es :$ ",presiofinal)
    
else :
    print("error de numero")

    
    





