print("Asignatura optativas Año 20024")
print("Asignatura optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
opcion = input("Escribe la asignatura escogida: ")

asignatura = opcion.lower()

if asignatura in ("informatica gráfica", "pruebas de software", "usabilidad y accesibilidada"):
    print("Asignatura elegida "+asignatura)
else:
    print("La asigantura escogida no está contemplada")