print("///CONVERSOR DE UNIDADES///")
print("que quiere covertir?")
print("1-kg a gm")
print("2-km a cm")
print("3-celsiu a fahrenheint ")
print("4-exit ")
ops=int(input(": "))

if ( ops == 1 ):
    
    print("kg a gm")
    deps=int(input("
    : "))
    
    
    
    print("deposito ",deps ,"ahora tiene",deposito," en su cuenta ")
    
elif ( ops == 2 ):
    print("km a cm")
    ret=int(input("cuanto quiere retorar : "))
    
    total= ret-saldo
    
    print("ya retiro:$ ", ret, " y le queda solo:$ ", total)
    
elif (ops == 3 ):
    print("celsiu a fahrenheint")
    print(" su saldo actual es:$ ", total)
    
elif  (ops == 4 ):
    print("gracias por usar nuestro servicios ")
    
else:
    print("error de numero ")
    
