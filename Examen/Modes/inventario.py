from services.productos import obtener_productos

inventario = []

def cargar_inventario_inicial():
    productos_iniciales = obtener_productos()
    for nombre, precio in productos_iniciales.items():
        inventario.append({'nombre': nombre, 'cantidad': 1, 'precio': precio})

def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
    else:
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")

def agregar_producto(nombre, cantidad, precio):
    inventario.append({'nombre': nombre, 'cantidad': cantidad, 'precio': precio})

