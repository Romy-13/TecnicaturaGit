punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
# print(punto)
if "lala" in punto:
    print("Hemos encontrado", punto)

print(punto.get("x"))
print(punto.get("lala", 97))

del punto["x"]
del [punto["y"]]
print(punto)

punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "Romina"},
    {"id": 2, "nombre": "Iris"},
    {"id": 3, "nombre": "Naira"},
    {"id": 4, "nombre": "Lautaro"}
]
for usuario in usuarios:
    print(usuario["nombre"])
