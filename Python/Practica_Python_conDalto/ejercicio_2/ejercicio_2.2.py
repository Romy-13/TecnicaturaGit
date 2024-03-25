# Obtener el nombre de un producto y su precio, he indicar el más caro y el más barato
def obtener_producto(cantidad_de_productos):
    productos =[]
    for i in range(cantidad_de_productos):
        nombre= input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        producto = (nombre,precio)
        productos.append(producto)
    productos.sort(key=lambda x:x[1])
    mas_barato= productos[0][0]  
    mas_caro = productos[-1][0]
    return mas_caro,mas_barato

mas_caro, mas_barato = obtener_producto(6)  
print(f"El producto más barato es: {mas_barato} y el producto más caro es: {mas_caro}")
