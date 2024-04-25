# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuación
# elimine los elementos repetidos, por último mostrar la lista

# Creamos una lista
lista = [1, 2, 3, "Ariel", 7, 7, 3, "Alberto", 1, "Ariel", 2, "Alberto"]
#conjunto = set(lista)#convertimos la lista a un conjunto de tipo set
#lista = list(conjunto)#convertimos el conjunto en lista
lista = list(set(lista))# La conversión hecha en una sola linea de código (eficiente)
print(lista)