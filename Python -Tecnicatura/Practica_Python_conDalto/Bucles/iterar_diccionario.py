diccionario = {
    "apellido": "Rodriguez",
    "nombre": "Romina",
    "edad": 36
}

#Recorriendo diccionariopara obtener la clave 
for key in diccionario:
    key 
    print(f"La clave es: {key}")

  #Recorriendo diccionario con items() para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    evalue = datos[1]
    print(f"La clave es: {key} y los valores son :{evalue}")