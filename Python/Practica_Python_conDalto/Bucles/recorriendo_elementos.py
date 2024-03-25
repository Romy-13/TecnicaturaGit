animales = ["gato","perro","loro","vaca",]
numeros = [10, 20, 30, 40]

#Recorriendo la lista animales
for animal in animales:
    print(f"Ahora la variable animal es:  {animal}")

#Recorriendo la lista números y multiplicando el valor *10
for numero in numeros:
    resultado = numero * 10
    print(resultado)  

#Recorremos dos lista al mismo tiempo
for numero,animal in zip(numeros,animales):
    print(f"recorremos lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")

#Forma no optima de recorrer una lista con su indice
for num in range(len(numeros)):
    print(numeros[num])    

#forma correcta de recorrer una lista con su indice
    for num in enumerate(numeros):
        indice = num[0]
        valor = num[1]
        print(f"ejecutando indice: {indice} y el valor es: {valor}")

#Usando el for/else
        for numero in numeros:
            print(f"ejecuntando el ultimo bucle, valor actual: {numero}")
        else:
            print("se termina el bucle")    

#se puede iterar tuplas, lista y conjuntos