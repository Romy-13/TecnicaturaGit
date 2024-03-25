#creando un conjunto con set
conjunto = set(["dato1","dato2"])

#metiendo un conjunto en otro conjunto
conjunto1 =frozenset(["dato 1","dato 2"])
conjunto2 = {conjunto1,"dato 3"}

#teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {2,4,6,7}

#verificar si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificamos si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#Verificamos si hay un elemento en común
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)