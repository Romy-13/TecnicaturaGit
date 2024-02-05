n1 = input("Ingresa el primer numero")
n2 = input("Ingresa un segundo numero")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los números {n1} y {n2},
el resultado de la suma es {suma},
el resultado de la resta es {resta},
el resultado de la miltiplicación es {multi},
y el resultado de la división es {div}"""

print(mensaje)
