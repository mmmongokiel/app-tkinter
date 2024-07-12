import tkinter as tk

# Función para manejar el clic del botón
def saludar():
    label_saludo.config(text="¡Hola, Mundo!")

# Crear la ventana principal
root = tk.Tk()
root.title("Esta es la ventana principal")

# Crear un botón
boton_saludar = tk.Button(root, text="Saludar", command=saludar)
boton_saludar.pack(padx=200, pady=200)

# Crear una etiqueta para mostrar el saludo
label_saludo = tk.Label(root, text="")
label_saludo.pack()

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()
