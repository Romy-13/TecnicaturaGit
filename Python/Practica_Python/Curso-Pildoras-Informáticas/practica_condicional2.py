print("Programa de becas Año 2017")
distancia_escuela = int(input("Introduce la distancia de la escuela en km: "))
print(distancia_escuela)

numero_hermanos = int(input("Introduce el número de hermanos en el centro: "))
print(numero_hermanos)

salario_familiar = int(input("Introduce el salario anual bruto: "))
print(salario_familiar)

if distancia_escuela> 40 and numero_hermanos>2 or salario_familiar<=20000:
    print("Tiene derecho a beca")
else:
    print("No tienes derecho a beca")