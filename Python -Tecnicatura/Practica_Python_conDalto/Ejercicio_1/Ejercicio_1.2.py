#Ejercicio 2:
#a)-Pedirle al usuario que diga cualquier texto real y:
#-calcular cuanto tardaría en decir esa frase
#-¿cuántas palabras dijo?

#b)-Si se tarda más de 1 minuto:
#-decirle para flaco:"tampoco te pedi un testamento"

#c)-Dalto habla un 30% más rápido:
#cuánto tardará él en decirlo

#Le pedimos al usuario que nos diga una frase o varias
frase = input("Decime una frase y te calculo cuanto tardaría si tuviera que decirla:  ")

#Creamos una lista con todas las palabras de la frase(se separan cada ves que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

#Usamos len() para saber cuantos elementos hay en una lista
cantidad_de_palabras = len(palabras_separadas)
print("----------------------------------------------")

#En caso que tarde mas de 1 minuto en decirlo, le decimo que pare
if cantidad_de_palabras > 120:
    print(f"Para flaco, tampoco te pedi un testamento")

#Calculamos cuánto tardaria en decir las palabras y se lo decimos:
print("------------------------------------------------")
print(f"Dijiste {cantidad_de_palabras} palabras y tardarías {cantidad_de_palabras/2} segundos en decirlas")
print(f"Dalto lo diría en {cantidad_de_palabras *100 //2 *1.3 / 100} segundos")