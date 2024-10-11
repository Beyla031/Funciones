from modes.agregar_producto import agregar_producto
from modes.eliminar_producto import eliminar_producto
from modes.mostrar_inventario import mostrar_inventario
from modes.mostrar_valor_total import mostrar_valor_total
from modes.actualizar_nombre import actualizar_nombre
from modes.actualizar_cantidad import actualizar_cantidad
from modes.actualizar_precio import actualizar_precio

def mostrar_menu():
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario")
        print("4. Mostrar valor total")
        print("5. Actualizar nombre")
        print("6. Actualizar cantidad")
        print("7. Actualizar precio")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")
