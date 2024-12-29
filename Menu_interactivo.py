from funciones import *
from tkinter import *

# Interfaz gráfica

# Configuración de la raíz
root = Tk()
root.title("Gestión de inventario")
# root.iconbitmap("")
root.resizable(True,True)

frame = Frame(root, width=480, height=320)
frame.pack()
frame.config(fill="both",expand=1)

# Bucle de la aplicación
root.mainloop()

# Menú interactivo

while True:
    try:
        print("Mensaje de bienvenida\n")
        n_menu = int(input("""Elija entre las siguientes opciones:
1 - Ver productos en el inventario
2 - Añadir un nuevo producto
3 - Actualizar la cantidad de un producto
4 - Eliminar un producto
5 - Generar resumen del inventario
6 - Salir del programa\n                                                                                                            
"""))
        if n_menu == 1:
            ver_productos()
            print("\n")
        elif n_menu == 2:
            nuevo_producto()
        elif n_menu == 3:
            modificar_cantidad()
        elif n_menu == 4:
            eliminar_producto()
        elif n_menu == 5:
            resumen_inventario()
        elif n_menu == 6:
            cierre()
            break
    except ValueError:
        print("Error: Error de valor")