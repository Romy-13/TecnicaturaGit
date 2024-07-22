salario_presidente = int(input("Introduce salario presidente: "))
print("Salario presidente: "+ str(salario_presidente))

salario_director = int(input("Introduce salario Director: "))
print("Salario Director: "+ str(salario_director))

salario_jefe_area = int(input("Introduce salario Jefe area: "))
print("Salario Jefe area: "+ str(salario_jefe_area))

salario_administrativo = int(input("Introduce salario administrativo: "))
print("Salario administrativo: "+ str(salario_administrativo))

#Operadores de condiciones concatenados
if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en la empresa")
