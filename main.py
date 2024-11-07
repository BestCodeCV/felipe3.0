import tkinter as tk
from ui import create_interface
import functions

# Lista para almacenar posiciones registradas
click_positions = []
program_running = False  # Variable de control para iniciar y detener el programa

# Funciones para los botones
def on_attack():
    message = functions.attack()
    show_message(message)

def on_multi_attack():
    message = functions.multi_attack()
    show_message(message)

def on_register():
    message = functions.register_sectors()
    show_message(message)

def on_start():
    message = functions.start()
    show_message(message)

def on_stop():
    message = functions.stop()
    show_message(message)

# Configurar la aplicación principal
root = tk.Tk()
root.title("Felipe 2.0")
root.geometry("260x300")
root.configure(bg="#2d2d2d")  # Fondo oscuro de la ventana principal

# Crear la interfaz y obtener la función para mostrar mensajes
show_message = create_interface(root, on_attack, on_multi_attack, on_register, on_start, on_stop)

root.mainloop()
