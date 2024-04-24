#creando una función que nos devuelva los numeros primos
#entre 0 y el argumento que pasamos

#Creamos una función para saber si un número es primo
def es_primos(num):
    #verificamos que el número pasado no pueda dividirse
    #por ningún número entre 2 y ese mismo número -1
    for i in range(2,num-1):
        #si es divisible por alguno retornamos false y termina el bucle
        if num%i==0: return False
    #si termina el bucle, significa que no fue divisible entonces es primo    
    return True    

#creamos función que retorne una lista con todos los primos
def primos_hasta(num):
    #creamos la lista
    primos =[]
    for i in range(3,num+1):
        #verificamos si el valor es primo
        resultado = es_primos(i)
        #en caso que lo sea lo agregamos a la lista
        if resultado == True: primos.append(i)
    #devolvemos la lista    
    return primos    

#creamos el resultado llamando a la función y lo mostramos
resultado = primos_hasta(13)
print(resultado)


#función para reducir el codigo de números primos
#primos_hasta = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0,5)+1)),range(2, num)))
#print(primos_hasta(15))