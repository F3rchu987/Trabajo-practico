print("_______________________________________")
print( "|   Bienvenido al software de calculo |")
print( "_______________________________________")

print( "cuantos kg de pan desea hacer hoy")
print("ATENCION NO INGRESAR MENOS DE 100 docenas")
cantidad=int(input("ingrese la cantidad" ))

harinag = 1200 / 2
harina2 = harinag * cantidad
harinakg = harina2/1000

ccg= 225/2
cc2= ccg*cantidad
litros=cc2/1000

levadurag=25/2
levadura2=levadurag*cantidad
levadurakg=levadura2/1000

huevo=1 * cantidad
huevou=huevo/2

azucarg=100/2
azucar2=azucarg*cantidad
azucarkg=azucar2/1000

mielg=15/2
miel2=mielg*cantidad
mielkg=miel2/1000

salg=10/2
sal2=salg*cantidad
salkg=sal2/1000

mantecag=200/2
manteca2=mantecag*cantidad
mantecakg=manteca2/1000

arinag = 25 / 2
arina2 = arinag * cantidad
arinakg = arina2/1000

print("_____________________________________________________")
print("la cantidades que necesitas serian las siguientes:"   )
print("       °Harina de trigo comun, de todo uso:", harinakg,"kg")
print("       °Agua templada:",litros,"lts"                  )
print("       °levadura:",levadurakg,"kg"                    )
print("       °huevo:",huevou,"cantidad"                     )
print("       °azucar:",azucarkg,"kg"                        )
print("       °miel:",mielkg,"kg"                            )
print("       °Sal:",salkg,"kg"                              )
print("       °manteca:",mantecakg,"kg"                      )
print("       °Harina para empaste:", arinakg,"kg"           )
print("_____________________________________________________")



