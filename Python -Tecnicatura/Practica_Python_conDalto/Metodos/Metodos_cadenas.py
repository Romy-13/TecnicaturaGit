cadena1 = "Hola soy Romina"
cadena2 = "Hola Mundo"


#convierte la cadena en mayúsculas
mayus= cadena1.upper()
#convierte la cadena en minúsculas
minus = cadena1.lower()
#coloca mayúscula a la primera cadena
primera_letra_mayus = cadena1.capitalize()
#busca una cadena en otra cadena, si no hay concidencia lanza un -1
busqueda_find = cadena1.find("e")
#busca una cadena en otra, si no hay concidencias larga una opción
busqueda_index = cadena1.index("R")
#si es numerico devuelve true y si no devuelve false
es_numerico = cadena1.isnumeric()
#si es alfa numerico, devuelve true y si no devuelve false
alfa_numerico = cadena1.isalpha() 
#contamos coincidencias de una cadena en otra cadena, contando las cincidencias
conteo_coincidencia = cadena1.count("a")
#contamos cuantos caracteres hay en una cadena
conteo_caracteres = len(cadena1)
#verifica se una cadena empieza con una cadena dada, si es asi su resultado es true
empieza_con = cadena1.startswith("H")
#verifica se una cadena termina con una cadena dada, si es asi su resultado es true
termina_con = cadena1.endswith("a")
#remplaza una parte de la cadena dada con otra dada
cadena_nueva = cadena1.replace("Hola","Buenas")
#separa cadena con las cadenas que le pasemos
cadena_separada = cadena1.split(",")


print(cadena_separada[0])

