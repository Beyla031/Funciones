# Tkither/importa la libreria 
import tkinter as tk

# CREAR UNA VENTANA
#para crear una ventan es necesari la intancia de metodo
#Tk de la libreria tkinter, almacena la instancia en una variable
mi_ventana = tk.Tk()
#utiliza el metodo tittle() para agregar un titulo a la ventana 
mi_ventana.title("Jossue Fuentes")
#utiliza el metodo geometry () para establecer un tamanno en pixceles 
mi_ventana.geometry("500x600")

# Crear un texto
#como argument agrega el nombre de tu ventana y el texto en la variable
etiqueta = tk.Label(mi_ventana, text="Hola Mundo")
# El metodo pack () muestra el objeto con caracteristicas basicas
etiqueta.pack()

#Muestra la venatana y se queda siempre al final
mi_ventana.mainloop()


