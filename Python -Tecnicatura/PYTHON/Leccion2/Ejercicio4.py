"""
Ejercicio 4: Etapas de la Vida
"""
edad = int(input("Ingrese su edad (0 - 60): "))
etapa = None
if 0 <= edad < 10:
    etapa = ("La inafancia es increible y bella")
elif 10 <= edad < 20:
    etapa = ("Tienes muchos cambios, mucho que estudiar")
elif 20 < edad <= 30:
    etapa = ("Amor y comienza el trabajo")
elif 30 < edad <= 40:
    etapa = ("una familia, crianza y responsabilidad")
elif 40 < edad <= 50:
    etapa = ("Etapa de aconsejar y disfrutar")
elif 50 < edad <= 60:
    etapa = ("Experiencia y descanso")
else:
    etapa = ("No hay mensaje para esta edad")
print(f"Para los años {edad} de vida, el mensaje es :  {etapa}  ")

