#Creando diccionario con dict
diccionario = dict(nombre="Romina", apellido="Rodriguez")

#Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario= {frozenset(["Romi","linda"]):"jajajaja"}

#Creando diccionarios con fromkeys con dos parámetros
diccionario = dict.fromkeys("ABCD","no sé")
#Creando un diccionario con fromkey: cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"],"no se")

print(diccionario) 