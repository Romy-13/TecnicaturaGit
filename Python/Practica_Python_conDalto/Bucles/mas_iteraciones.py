#Creando iteraciones
frutas = ["banana", "manzana","pera","ciruela","granada", "durazno"]
cadena = "Hola Mundo"
numeros=[2, 6, 10, 25]

#evitando que se coma una fruta con la sentencia continue
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f"me voy a comer una fruta: {fruta}")

#evitando que el bucle siga ejecutandose
for fruta in frutas:
    print(f"me voy a comer una {fruta}")
    if fruta == "pera":
        break
print("bucle terminado")    

#iterando cadena de texto
for letra in cadena:
    print(letra)

#for en varias lineas de codigo
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero*2)

print(numeros_duplicados)    

#for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
