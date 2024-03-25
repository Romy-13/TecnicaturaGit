#creando una lista (se puede modificar)
lista = ["Romina","Soy estudiante","tengo 35años",True,1.65]

#creando una tupla (no se puede modificar)
tuple = ["Romina","Soy estudiante","tengo 35años",True,1.65]

#Esto es valido
#lista[3] = "Maquinola"
#Esto no es valido
#tuple[3] = "Maquinola"

#print(lista[0])
#Creando un conjunto (set) no se accede a elementos por indice, no almacena datos duplicados
conjunto ={"Romina","Soy estudiante","Tengo 35 años",True,1.65 }
#print(conjunto[1]) no puedo acceder al elemento

#creando un diccionario(dick) la estructura es keey : evalue y separados por comas
diccionario ={
    "nombre":"Romina",
    "canal": "Soy estudiante",
    "estas_emocionado": True,
    "altura":1.65

}
print(diccionario["altura"])