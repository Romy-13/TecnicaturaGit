# Para abrir un archivo declaramos una variable

try:
    archivo = open("prueba.txt", "w", encoding="utf8")# La 'w' es de write=escribir
    archivo.write("Programamos con diferentes tipos de archivos, ahora en txt.\n")
    archivo.write("Los acentos son importantes para las palabras\n")
    archivo.write("Como por ejemplo: acción, ejecución, producción\n")
    archivo.write("Las letras para cada modificación son:\nr read leer, \na append anexa, \nw write escribe, \nx crea un archivo")
    archivo.write("\nt para texto o text, \nb archivos tipos binarios, \nw+ para escribir y leer info, igual que r+ \n")
    archivo.write("Saldos a todos los alumnos de la Tecnicatura\n")
    archivo.write("Con esto terminamos")
except Exception as e:
    print(e)
finally: #siempre se ejecuta
    archivo.close()#con esto se debe cerrar el archivo
# archivo.write("todo queda perfecto")  esto en un error, porque el archivo está cerrado