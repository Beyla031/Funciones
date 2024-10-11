from services.inventario import productos

def actualizar_precio(nombre, nuevo_precio):
    if nombre in productos:
        productos[nombre]['precio'] = nuevo_precio
        print(f"Precio del producto '{nombre}' actualizado a {nuevo_precio:.2f}.")
    else:
        print(f"Producto '{nombre}' no encontrado.")
