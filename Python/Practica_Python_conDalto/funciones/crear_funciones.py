#creando funciones simples
#def saludar():
#    print("Hola Romina ¿cómo estás?")

#saludar()

#crear una función que tenga parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if(sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = "amor"
    
    
    print(f"Hola {nombre}, mi {adjetivo} ¿cómo estás?") 

saludar("Carlos", "Hombre")
saludar("Romina","mujer")
saludar("Frank", "no binario")

#crear una función que nos retorne multiples  valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 =num -2
    c2 = num
    c3 = num-5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num

#desempaquetando la función
passwor,primer_numero = crear_contraseña_random(981)   

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es: {passwor}")  
print(f"el número utilizado para crearla fue: {primer_numero}")