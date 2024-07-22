#edad=int(input("Introduce tu edad por favor: "))
import math

#while edad<5 or edad>100:
#    print("Has introducido una edad incorrecta. Vuelva a introducirlo")
#    edad = int(input("Introduce tu edad por favor: "))

#print("Gracias por colaborar")
#print("Edad del aspirante: "+ str(edad))


import math
print("Programa de calculo de raiz cuadrada")
numero=int(input("Introducir un número por favor: "))

intentos=0

while numero<0:
    print("No se puede hallar la raiz cuadrada de un número negativo")

    if intentos==2:
        print("Has consumido demasiados intentos. El programa a finalizado")
        break

    numero= int(input("Introducir un número por favor: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de "+ str(numero)+" es "+ str(solucion))