from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):#Este es un método para aprender lo que es el polimorfimos
    # print(objeto) # De manera indirecta llama al str de la clase Empleado o Gerente
    print(type(objeto)) # Esto es para saber el tipo de dato recibe
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento);

empleado = Empleado('Romina', 400000)
imprimir_detalles(empleado)

gerente = Gerente('Natalia', 500000, 'Sistema')
imprimir_detalles(gerente)


