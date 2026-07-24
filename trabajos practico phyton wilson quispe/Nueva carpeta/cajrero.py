print("///CAJERO AUTOMATICO///")
saldo=1000
print("Que quiere saber hoy ")
print("1-DEPOSITO")
print("2-RETIROS")
print("3-CONSULTAR SALDO ")
print("4-exit ")
ops=int(input(": "))

if ( ops == 1 ):
    
    print("DEPOSITO")
    deps=int(input("cuanto quiere depositar: "))
    
    deposito=saldo+deps
    
    print("deposito ",deps ,"ahora tiene",deposito," en su cuenta ")
    
elif ( ops == 2 ):
    print("RETIROS")
    ret=int(input("cuanto quiere retorar : "))
    
    total= ret-saldo
    
    print("ya retiro:$ ", ret, " y le queda solo:$ ", total)
    
elif (ops == 3 ):
    print("SALDO")
    print(" su saldo actual es:$ ", total)
    
elif  (ops == 4 ):
    print("gracias por usar nuestro servicios ")
    
else:
    print("error de numero ")
    
    