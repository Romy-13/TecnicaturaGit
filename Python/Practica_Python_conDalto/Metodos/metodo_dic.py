diccionario = {
    "nombre" : "Romina",
    "apellido" : "Rodriguez",
    "subs" :1000
}
#keys: devuelve las claves(también sirve para iterar)
claves = diccionario.keys()

#obteniendo un elemento con get()(si no encuentra nada el programa continúa)
claves = diccionario.get("nombre")

#eliminando todo el diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("subs")

#obteniendo un elemento edic_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)


