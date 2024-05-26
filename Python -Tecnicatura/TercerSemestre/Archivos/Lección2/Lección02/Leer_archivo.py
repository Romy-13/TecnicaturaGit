
archivo = open("prueba.txt", "r", encoding="utf8",)
#print(archivo.read())
#print(archivo.read(15))
#print(archivo.read(5))
#print(archivo.readline())

#Vamos a iterar en lineas:
#for linea in archivo:
    #print(linea): iteramos todos los elementos del archivo
    #print(archivo.readlines())# accedemos a los archivos como una lista
#print(archivo.readlines()[3])

#Anexamos información, copiamos a otro
archivo2 = open("copi.txt", "w", encoding="utf8")
archivo2.write(archivo.read())
archivo.close()#cerramos el primer archivo
archivo2.close()#cerramos el segundo archivo

print("Se ha terminado el proceso de leer y copiar archivo")