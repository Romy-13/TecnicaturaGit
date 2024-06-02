"""Introdución a Python"""
print("""Función con parámetros""")


def suma(num1, num2):
    #print(num1 + num2)- una de las maneras de mostrar el resultado
    resultado = num1+num2 # otra manera es crando una variable

    return resultado

#una manera de llamar a la función y mostrarla
#print(suma(5, 7))
#print(suma(4, 10))
#print(suma(22, 90))

#Otra manera de llamar a la función y mostrarla
almacena_resultado=suma(3,6)
print(almacena_resultado)