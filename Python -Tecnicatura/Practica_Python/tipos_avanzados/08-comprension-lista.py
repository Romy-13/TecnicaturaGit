usuarios = [
    ["Lucas", 4],
    ["Lauti", 1],
    ["Nai", 5]
]
# nombres = []
# for usuario in usuarios:
#    nombres.append(usuario[0])
# print(nombres)

# map
# nombres = [usuario[0] for usuario in usuarios]

# filtrar-filter
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# nombres = list(map(lambda usuario: usuario[0], usuarios))

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
