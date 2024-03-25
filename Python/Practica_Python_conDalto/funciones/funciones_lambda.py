numeros =[1,2,3,4,5,6,7,8,9,11,13,14,15,16,20]

#creamos una función lambda para mutiplicar por 2
multiplicar_por_dos = lambda x: x*2

#creamos una función para que nos diga si es par
#def es_par(num):
#    if (num%2==0):
#        return True

#usando filter con una función común
#numeros_pares = filter(es_par,numeros)

#creando lo mismo que antes pero con lambda

numeros_pares = filter(lambda numero:numero%2 == 0,numeros)

print(list(numeros_pares))