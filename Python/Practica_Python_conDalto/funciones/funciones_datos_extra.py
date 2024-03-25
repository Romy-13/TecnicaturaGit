#creando una función de 3 parametros
#def frase(nombre,apellido,adjetivo):
#    return f"Hola {nombre} {apellido} sos muy {adjetivo}"

#utilizando keywords arguments
#frase_resultante = frase("Romina", "Rodriguez","inteligente")

#creando la misma función con parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo="linda"):
    return f"Hola {nombre} {apellido} sos muy {adjetivo}"

frase_resultante = frase("Romina", "Rodriguez", "inteligente")
print(frase_resultante)