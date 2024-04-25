import figuraGeometrica
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


print("Creación del objeto clase cuadrado".center(50, '-'))
cuadrado1 = Cuadrado(8, "Azul")
cuadrado1.alto = 7
cuadrado1.ancho = 7
# print(cuadrado1.ancho)
# print(cuadrado1.alto)
print(f"Cálculo del área del cuadrado: {cuadrado1.calcular_area()}")

# MRO = Metodo Resolición Orden
# print(Cuadrado.mro())

print(cuadrado1)
print()
print("Creación del objeto clase rectángulo".center(50,'-'))
rectangulo1 = Rectangulo(3, 4, 'verde')
rectangulo1.ancho = 8
rectangulo1.alto = 9
print(f'Calcular area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

# figura1 = figuraGeometrica() No se puede instanciar, es abstracta