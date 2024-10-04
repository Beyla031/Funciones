
tareas = [
    ("Estudiar para el examen", "Revisar capítulos 1 a 5", "en progreso"),
    ("Hacer ejercicio", "Ir al gimnasio por 1 hora", "completada"),
    ("Llamar al médico", "Solicitar una cita para chequeo", "pendiente"),
    ("Enviar el informe", "Enviar el informe a mi jefe por correo", "en progreso")
]

def mostrar_menu():
    print("\nBienvenido al sistema de gestión de tareas")
    print("1. Agregar tareas")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("0. Salir")
    return input("Ingrese una opción: ")

def agregar_tarea(tareas):
    nombre = input("Ingrese el nombre de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    estado = "pendiente"
    tareas.insert(len(tareas), (nombre, descripcion, estado))
    print("Tarea agregada exitosamente.")

def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    indice = int(input("Ingrese el índice de la tarea a eliminar: "))
    if 0 <= indice < len(tareas):
        tareas.pop(indice)
        print("Tarea eliminada exitosamente.")
    else:
        print("Índice no válido.")

def mostrar_tareas(tareas):
    print("\nLista de tareas:")
    for i, tarea in enumerate(tareas):
        print(f"{i}. {tarea[0]} - {tarea[1]} - {tarea[2]}")

while True:
    opcion = mostrar_menu()
    if opcion == "1":
        agregar_tarea(tareas)
    elif opcion == "2":
        eliminar_tarea(tareas)
    elif opcion == "3":
        mostrar_tareas(tareas)
    elif opcion == "0":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
