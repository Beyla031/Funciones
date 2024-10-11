from services.inventario import productos

def mostrar_valor_total():
    total = 0
    for detalles in productos.values():
        total += detalles['cantidad'] * detalles['precio']
    print(f"Valor total del inventario: {total:.2f}")
