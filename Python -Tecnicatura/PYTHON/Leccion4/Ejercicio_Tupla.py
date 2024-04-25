import math #Importamos las clase math para hacer uso dela función sqr (raiz cuadrada)
# Dada la siguiente tupla:
tupla = (13, 1, 8, 3, 2, 5, 8)
# Crea una lista que solo incluya los números menores a 5
# e imprima por consola[1,3,2]
lista = []
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)


# Ejercicio de Matematicas
# Para sacar la raiz cuadrada de un número positivo
numero = int(input("Digite un número positivo: "))
while numero < 0:
    print("Error-> Debería ser un número positivo")
    numero = int(input("Digite un número positivo: "))
print(f"\nSu raiz cuadrada es : {math.sqrt(numero):.2f}")


