#forma no optima de sumar valores
#def suma(lista):
#    numeros_sumados= 0
#    for numero in lista:
#        numeros_sumados = numeros_sumados + numero
#    return numeros_sumados

#resultado = suma([5,3,4,9,10,20,3])


#forma optima de sumar valores
def suma_total(numeros):
    return sum(([*numeros]))

resultado2 = suma_total([5,3,9,10,20,3])
print(resultado2)    


#lo mismo de arriba pero utilizando el operador * como argumento  (*args)
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus números es: {sum(numeros)}"

resultado = suma("Romina",5,3,9,10,20,3)

