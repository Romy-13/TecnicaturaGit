# for cumple multiple finciones, sobre todo
# para iterar una lista de elementos,
# buscar elementos, realizar operaciones matemáticas, ect
buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("no encontre el numero buscado :(")

for char in "Ultimate Python":
    print(char)
