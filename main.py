import tkinter as tk
from ui import create_interface
import functions
import threading
from tkinter import ttk
# Lista para almacenar posiciones registradas
click_positions = []

program_running = False  # Variable de control para iniciar y detener el programa
detection_thread = None

red = "#cc0000"
green = "#3eaa05"
white = "#ffffff"

# Funciones para los botones
def on_attack():
    functions.attack(show_message)

def on_multi_attack():
    message = functions.multi_attack()
    show_message(message, white)

def on_register():
    message = functions.register_sectors()
    show_message(message, white)

def on_start():
    global detection_thread
    if not detection_thread or not detection_thread.is_alive():
        detection_thread = threading.Thread(target=functions.start_detection, args=(show_message,))
        detection_thread.start()
    else:
        show_message("La detección ya está en curso.")

def on_stop():
    message = functions.stop()
    show_message(message, red)

# Configurar la aplicación principal
root = tk.Tk()
root.title("Felipe 2.0")
root.geometry("260x300")
root.configure(bg="#2d2d2d")  # Fondo oscuro de la ventana principal
show_message = create_interface(root, on_attack, on_multi_attack, on_register, on_start, on_stop)

root.mainloop()
