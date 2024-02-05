def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 7)
suma(1, 5)
suma(23, 45, 3)
