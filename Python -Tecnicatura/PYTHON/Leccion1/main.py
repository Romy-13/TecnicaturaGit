'''
miVariable = 3
print(miVariable)
miVariable = "Hola a todos los estudiantes de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
# Las literales se escriben con x344, la variable y = x088, la variable z = x408
print(id(y))
print(id(z))

a = False
print(type(a))
# Tips int, float, bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas(String)
miGrupoFavorito = "Divididos"
caracteristicas = "La mejor banda de rock"
print("Mi grupo favorito es:" + miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))

# Tipos de Boleanos(bool)
miBoleano = 1 > 2
print(miBoleano)

if miBoleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario
# función input
resultado = input("digite un numero: ")  # regresa un dato tipo string
print(resultado)

# Conversión de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
'''
from typing import Union, Any

"""
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
#print("Resultado de la suma:",suma)
print(f"El resultado de la suma es: {suma}")

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es:{multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la division es: {division}")
division = operandoA // operandoB
print(f"El resultado de la division (int) es: {division}")
modulo = operandoA % operandoB
print(f"El resultado de division o residuo (modulo) es: {modulo}")
exponente = operandoA ** operandoB
print(f"El resultado de la exponente es: {exponente}")
"""
"""
alto = int(input("Proporciona el alto del rectangulo: "))
ancho = int(input("Proporcione el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print("area: ", area)
print("perimetro: ", perimetro)
"""
"""
# Operadores de asignación
miVariable3 = 10
print(miVariable3)

# Operadores de reasignación

miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable3 * 3
miVariable3 *= 3
print(miVariable3)

# miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)

# Operadores de comparación
d = 4
b = 2
resultado = d == b #comparamos si son iguales
print(resultado)

# OPerador diferente
resultado = d != b
print(resultado)

# operador mayor que
resultado = d > b
print(resultado)

# operador menos que
resultado = d < b
print(resultado)

# Operador es mayor o igual que
resultado = d >= b
print(resultado)

# Operador es menos o igual que
resultado = d <= b
print(resultado)

# Ejercicio: número par e impar
a = int(input("digite un numero: "))
print(f"el residuo de la division es: {a % 2}")
if a % 2 == 0:
    print(f"el valor de a es: {a} es un numero par")
else:
    print(f"el valor de a es : {a} es un numero imparar")
 """
"""
# Ejercico: determinar si es mayor de edad

edadAdulto = 18
edadPersona = int(input("digite su edad"))
if edadPersona >= edadAdulto:
    print(f"su edad es: {edadAdulto} es mayor de edad")
else:
    print(f"su edad es: {edadAdulto} es menor de edad")
 """
"""
# Operadores Lógicos
a = True
b = True
resultado = a and b
print(resultado)

# OPerador or
resultado = a or b
print(resultado)

# Operador not
resultado = not a
print(resultado)
"""
"""
# Ejercicio: valor de rango
valor = int(input("digite un numero: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = valor >= valorMinimo and valor <= valorMaximo
if dentroRango:
    print(f"el valor {valor} esta dentro de rango")
else:
    print(f"el valor {valor} No esta dentro de rango")
 """
"""
# Ejercicio: operador or
vacaciones = False
diaDescanso = False
if vacaciones or diaDescanso:
    print("puede asistir")
else:
    print("tiene trabajo que hacer")
"""
"""
# Ejercico: rango entre las edades 20 y 30
edad = int(input("digite su edad"))
veinte = edad >= 20 and edad < 30
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)

if veinte or treinta:
    print("estas dentro del rango de los (20\'0) años")
elif treinta:
    print("estas dentro del rango de los (30\'0) años")
else:
    print("no estas dentro del rango de los (20\'0) a (30\'0) años")
"""
"""
# Ejercicio:mayor de 2 números
numero1 = int(input("digite el valor del numero 1: "))
numero2 = int(input("digite el valor del numero 2: "))

if numero1 > numero2:
    print("el numero 1 es el mayor")
else:
    print("el numero 2 es el mayor")
"""
"""
# Ejercicio: tienda de libro
print("digite los siguientes datos del libro")
nombre = input("digite el nombre del libro: ")
id = int(input("digite el ID del libro: "))
precio = float(input("digite el precio del libro: "))
envioGratuito = input("indicar si el envio es gratuito (False/True): ")
if envioGratuito == True:
    envioGratuito = True
elif envioGratuito == False:
    envioGratuito = False
else:
    envioGratuito = "el valor es incorrecto, debe escribir True/False"
print(f'''
       Nombre: {nombre}
       ID: {id}
       Precio: {precio}
       Envio Gratuito?: {envioGratuito}
''')
"""




