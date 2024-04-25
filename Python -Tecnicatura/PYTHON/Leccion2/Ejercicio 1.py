"""
Ejercicio 1:
Debemos plasmar la expresión en una expresión
algoritmica, o sea hacer un código
"""
a = float(input("Digite el valor de a: "))
b = float(input("Digite el valor de b: "))
c = float(input("Digite el valor de c: "))
resultado = (a ** 3 * (b ** 2 - 2 * a * c)) / (2 * b)
print(f"El resultado es: {resultado}")

import math

"""
Ejercicio 2:
Determinar la solución lógica de la siguiente 
operación

a = float(input("Digite un valor para a: "))
b = float(input("Digite un valor para b: "))
resultado = ((3 + 5 * 8) < 3 and ((-6 / 3 * 4) + 2 < 2)) or (a > b)
print(f"El resultado es: {resultado}")
"""

"""
Ejercicio 3:
Intercambiar el valor de dos variables
Ejemplo: a=10   a=5
         b=5    b=10

a = 10
b = 5
print("Valor original:")
print("a =", a)
print("b =", b)

temp = a
a = b
b = temp
print("Intercambiar valores:")
print("a =", a)
print("b =", b)
"""
"""
Ejercicio 4: Área y longitud de un circulo
Hacer un programa para ingresar el radio de 
un circulo y se reporte su área y la longitud
de la circunferencia
"""
radio = float(input("Dijite el valor del radio: "))
area = math.pi * radio ** 2
longitud = 2 * math.pi * radio
print(f"El área del circulo es: {area}")
print(f"La longitud del circulo es: {longitud}")



