numeros = [2, 3, 4, 5, 1, 22, 32, 11]

# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True)
print(numeros2)


usuarios = [
    [4, "Lucas"],
    [1, "Lauti"],
    [2, "Nai"]
]


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=lambda el: el[1])
print(usuarios)
