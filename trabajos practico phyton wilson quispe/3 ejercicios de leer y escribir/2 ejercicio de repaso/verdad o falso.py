print("1- algunas flechas que apuntan hacia abajo estan rellenados de color verde")
num1=int(input("1-verdadero o 2 falso: "))

if(num1 == 1):
    print("yes")
    resp=+1
else:
    print("no")
    resp=0
print("2- ningun rombo es de color rojo  ")
num2=int(input("1-verdadero o 2 falso: "))

if(num2 == 1):
    print("yes")
    resp2=+1
    
else:
    print("no")
    resp2=0

print(" 3- todas las figuras rellenas de color violeta son flechas ")
num3=int(input("1-verdadero o 2 falso: "))

if(num3 == 1):
    print("yes")
    resp3=+1
else:
    print("no")
    resp3=0
    
print("4- algunas figuras de borde punteado son circulos")
num3=int(input("1-verdadero o 2 falso: "))

if(num3 == 1):
    print("yes")
    resp4=+1
else:
    print("no")
    resp4=0


total=resp+resp2+resp3+resp4
    
print("total ",total)
