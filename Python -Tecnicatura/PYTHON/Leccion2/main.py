# En esta clase veremos la sentencia if/else
"""condicion = 10
if condicion == True:
    print("condicion verdadera")
elif condicion == False:
    print("condicion es falsa")
else:
    print("condicion sin especificar")
"""
"""
# Conversión de número a texto
num = int(input("Digite un número en el rango del 1 al 3: "))
numTexto = " "
if num == 1:
    numTexto = "Número 1"
elif num == 2:
    numTexto = "Número 2"
elif num == 3:
    numTexto = "Número 3"
else:
    numTexto = "Has ingresado un número fuera de rango"
print(f"El número ingresado es: {num} = {numTexto}")
"""

# Operardor ternario
condicion = True
"""if condicion:
    print("condicion verdadera")
else:
    print("condicion falsa") 
"""
print("condicion verdadera") if condicion else print("condicion falsa")