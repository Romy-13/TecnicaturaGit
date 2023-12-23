'''
Sintaxis de range(inicio<opcional>, fin <requerido>, incremento <opcional>

'''
#Ejercicio 1: Crear un rango de 3 a 10 pero con incremento de 2 en 2, en un lugar de 1 en 1
#Ejemplo de ejecución: 3,5,7,9
print("Rango con valores de inicio en 3 y fin en 10, con incremento s¿de 2")
for i in range(3, 11, 2):
    print(i)

#Ejercicio 2: Iterar un rango de o a 10 e imprimir números divisibles
#Ejemplo de ejecución: 0,3,6,9

print("Rango de 0 a 10 con números devisibles entre 3")

for i in range(11):
    if i % 3 == 0:
        print(i)
        
#Ejercicio 3: Crear un rango de números de 2 a 6 e imprimirlos
#Ejemplo de ejecución: 2,3,4,5,6
print("Rango con valor de inicio= 2 y fin en 6")
rango = range(2, 7)
for i in rango:
    print(i)
