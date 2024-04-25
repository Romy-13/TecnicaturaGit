# Ingresa "N" enteros, visualizar la suma de los numeros
# pares de la lista, cuántos números pares existen y cuál
# es el promedio de los números impares

n = int(input("Dijite la cantidad de elementos a ingresar: "))
suma_pares = 0
conteo_pares = 0
suma_impares = 0
conte_impares = 0
for i in range(n):
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        suma_pares += numero
        conteo_pares += 1
    else:
        suma_impares += numero
        conte_impares += 1
print("La suma de los números pares es: ", suma_pares)
print("Cantidad de numeros pares es: ", conteo_pares)
print("El promedio de números impares es: ", conte_impares)














