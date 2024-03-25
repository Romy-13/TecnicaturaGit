#Falto el profesor y los alumnos vana a armar la clase

#pedir el nombre y la edad de los compañeros que asistieron a la clase

#función para obtener el asistente y al profesor segun la edad
def obtener_compañeros(cantidad_de_compañeros):

    #creamos una lista con los compañeros
    compañeros = []

    #ejecutamos un ciclo for para pedir información de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingres el nombre del compañero: ")
        edad = input("Ingrese la edad del compañero: ")
        compañero = (nombre,edad)

        #agregamos la información a la lista
        compañeros.append(compañero)

    #ordenandolos de menor a mayor según su edad    
    compañeros.sort(key=lambda x:x[1])

    #compañeros[x] devuelve una tupla con su (nombre y edad) y después accedemos al nombre
    #para definir el asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]  

    #retornamos en una tupla
    return asistente,profesor  

#desempaquetamos lo que nos retorna la función
asistente,profesor = obtener_compañeros(5)

#mostramos el resultado
print(f"El profesor es: {profesor} y su asistente es: {asistente}")


 
