#creando una lista con lis
lista = list(["Hola","Cómo estás?",35])

#acceder al elemento por indice
primer_elemento = lista[0] #devueleve "hola"

#modificar una elemento de la lista
lista[1] = "como has estado"

#devuelve la cantidad de elementos de una lista(longuitud de la lista)
cantidad_elemento = len(lista)

#agregando un elemento al final de la lista
lista.append("Romina")

#agregando un elemento en un indice especifico
lista.insert(2,"Linda")

#agregando varioas elementos a la lista
lista.extend(["Hermoso","Dia"])

#eliminando un elemento de la lista desde su indice
lista.pop(3)#con -1 para eliminar el último,con -2 para eliminar el penúltimo, y asi sucesivamente

#removiendo un elemento de la lista por su valor
lista.remove("Romina")

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando la lista em forma ascendente(si utilizamos el parametro reverse=true muestra la cadena al reves)
lista.sort()

#invirtiendo los elementos de la lista
lista.reverse()

# verificar si un elemento esta en la lista
esta_en_lista = 35 in lista #dependiendo la verificación sera true/false

print(esta_en_lista)
