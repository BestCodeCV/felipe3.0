# ui.py
import tkinter as tk

def create_interface(root, on_attack, on_multi_attack, on_register, on_start, on_stop):
# Variables de configuración para las velocidades
    
    #colors
    red = "#cc0000"
    green = "#3eaa05"
    white = "#ffffff"

    #styles
    button_style = {"bg": "#4a4a4a", "fg": "#ffffff", "font": ("Roboto", 10, "normal"), "width": 15, "height": 1, "pady": 5}
    small_button_style = {"width": 10, "height": 1, "font": ("Roboto", 9, "normal")}
    
    log_text = tk.Text(root, height=3, width=35, bg="#3e3e3e", fg="#ffffff", font=("Roboto", 10, "normal"))
    log_text.pack(pady=(10, 15))
    log_text.config(state=tk.DISABLED)

    def show_message(message, color=white):
        log_text.config(state=tk.NORMAL)
        log_text.delete("1.0", tk.END)
        log_text.tag_configure("color", foreground=color)
        log_text.insert(tk.END, message, "color")
        log_text.config(state=tk.DISABLED)
    # Side bar para sliders
    

# Etiquetas y sliders

    # Llamamos a set_sleep_durations con los valores actuales de los sliders
        #functions.set_sleep_durations(sleep_duration_1.get(), sleep_duration_2.get())

    tk.Button(root, text="Atacar", command=on_attack, **button_style).pack(pady=5)
    tk.Button(root, text="Ataque Múltiple", command=on_multi_attack, **button_style).pack(pady=5)
    tk.Button(root, text="Registrar Sectores", command=on_register, **button_style).pack(pady=5)
    
    tk.Button(root, text="Stop", command=on_stop, bg=red, fg="#ffffff", **small_button_style).pack(side=tk.LEFT, padx=10, pady=20)
    tk.Button(root, text="Encender", command=on_start, bg=green, fg="#ffffff", **small_button_style).pack(side=tk.RIGHT, padx=10, pady=20)
    
    return show_message
