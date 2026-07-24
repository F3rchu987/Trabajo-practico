print("Opción 1- Gramos a Kilogramos")
print("Opción 2- Celsius(C°) a kelvin(K)")
print("Opción 3- Mililitros a Litros")
unidad=int(input("¿Que traspaso de unidad deseas utilizar?:"))
if unidad==1:
    medida=float(input("Ingrese la medida que desea pasar de unidada:"))
    kilo=medida/1000
    print(medida,"G"," son ", kilo,"KG")
elif unidad==2:
    medida1=float(input("Ingrese la medida que desea pasar de unidada:"))
    kelvin= medida1+273.15
    print(medida1,"°C", " son ", kelvin,"K")
if unidad==3:
    medida2=float(input("Ingrese la medida que desea pasar de unidada:"))
    litro=medida2/1000
    print(medida2," ML ", "son ", litro,"Lts")