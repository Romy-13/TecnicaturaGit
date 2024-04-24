#Lista []
nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[-1])#para poder ver el último elemento de la lista
print(nombres[-2])#para poder ver el penúltimo

# Recuperar un rango de la lista
print(nombres[0:2])#solo muestra los indice 0, 1 pero no el indice 2
print(nombres[ :3])# indeces a mostrar 0, 1, 2
# Desde el indice indicado hasta el final
print(nombres[1: ])
#Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
# Iterar una lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

#Preguntamos cuantos elementos tiene
print(len(nombres))

# Agregamos un elemento
nombres.append('Marcela')
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Iris')
print(nombres)

# Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

#Eliminar el último elemento
nombres.pop()
print(nombres)

#Eliminar un indice especifico
del nombres[2] #del significado delete(eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#Eliminar la lista
del nombres
print(nombres)