# Calcular el factorial de un número mayor o igual a 0
num = int(input("dijite un número: "))
factorial = 1
if num < 0:
    print("El factorial no está definido para números negativos")
else:
    while num > 0:
        factorial *= num
        num -= 1
    print(f"El factorial es: {factorial}")

