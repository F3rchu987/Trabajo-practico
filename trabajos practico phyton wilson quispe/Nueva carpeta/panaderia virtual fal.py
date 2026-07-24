print("///PANNADERIA VIRTUAL//")
print("eliga uno de estos cuatroo productos ")
print("1-$2000 por una  docenas de pan")
print("2-$540 por una medialuna")
print("3-$350 por tortitas")
print( "4-$780 facturas de pan con relleno de chocolate")
ops=int(input(": "))

if ( ops == 1 ):
    pan=int(input("cuantoquiere llevar : "))
    
total= pan*2000
descuento=total* 0.15
presiofinal=total-descuento

print("el precio del producto :$ ", presoifinal)

elif ( ops == 2 ):
    
    luns=int(input("cuantos medialunas quiere llevar?"))
    
    total= luns*540
    descuento=total*0.15
    presiofinal=total-descuento
    
    print("el preco del prducto:$ ",presiofinal)
    
elif ( ops == 3):
    tort=int(input("cuantas tortitas quiere llevar"))
    
    total= tort*350
    descuento=total*0.15
    presiofinal=total-descuento
    
    print("el preco del producto:$ ",presiofina)
    
elif ( ops == 4 ):
    fac=int(input("cuantas quiere llevar ?"))
    
    total= fac*780
    descuento=total*0.15
    presiofinal=total-descuento
    
    print("el precio del producto:$ ",presiofinal)
    
else:
    print("numero incorrecto ")

    
    
    
    
    
    
    
    
    
    
    
