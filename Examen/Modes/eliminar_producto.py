from ..Services.inventario import productos

def eliminar_producto(nombre):
    if nombre in productos:
        del productos[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"Producto '{nombre}' no encontrado.")