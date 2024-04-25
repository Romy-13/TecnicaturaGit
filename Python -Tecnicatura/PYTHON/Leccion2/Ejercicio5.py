"""
Ejercicio 5: Sistema de calificaciones
"""
calif = int(input("Dijite un número pra calificación(1 -10): "))
if 9 <= calif <= 10:
    print("A")
elif 8 < calif <= 9:
    print("B")
elif 7 < calif <= 8:
    print("C")
elif 6 < calif <= 7:
    print("D")
elif 0 < calif <= 6:
    print("F")
else:
    print("El valor ingresado es incorrecto")
