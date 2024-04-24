mascotas = ["Pelusa", "Wolgang", "Pulga","Felipe","Toto",]

#Para agregar elementos
mascotas.insert(1, "Melvin")
mascotas.append("Maya")

#Para quitar elementos
mascotas.remove("Pulga")
mascotas.pop(1)
del mascotas[0]
mascotas.clear()
print(mascotas)