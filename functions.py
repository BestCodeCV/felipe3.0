#Configurar el tiempo entre 0.1 a 1 
tiempo_antes_de_la_accion = 0.2
tiempo_despues_de_accion = 0.0
tiempo_entre_cada_captura = 0.25


program_running = False

red = "#cc0000"
green = "#3eaa05"
white = "#ffffff"

show_message_func = None  

def attack(show_message):
    show_message("bebita ", white)
    return "Sector atacado"

def multi_attack():
    show_message_func("Ejecutando ataque múltiple...")
    return "Ataque múltiple ejecutado"

def register_sectors():
    show_message_func("Registrando sectores...")
    return "Sectores registrados"

def start():
    global program_running
    program_running = True
    show_message_func("Sistema encendido")
    return "Sistema encendido"

def stop():
    global program_running
    program_running = False
    show_message_func("Sistema detenido")
    return "Sistema detenido"


import pyautogui
import cv2
import numpy as np
import time
import keyboard

screen_width, screen_height = pyautogui.size()

posInicio = 0
posLife = 1
posEndBattle = 2
posNextBattle = 3
posReward = 4 
posAttack = 5

posRecent = -1

scale_factor = 0.4  

region_width = int(screen_width * 0.7) 
region_height = screen_height           

left = 0      
top = 0   

count = 0

templates = {
    "recompensa": cv2.resize(cv2.imread("src/recompensa.png", cv2.IMREAD_GRAYSCALE), None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA),
    "inicio": [
        cv2.resize(cv2.imread("src/inicio.png", cv2.IMREAD_GRAYSCALE), None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA),
        cv2.resize(cv2.imread("src/inicio2.png", cv2.IMREAD_GRAYSCALE), None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA),
        cv2.resize(cv2.imread("src/inicio3.png", cv2.IMREAD_GRAYSCALE), None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)
    ],
    "life": cv2.resize(cv2.imread("src/life.png", cv2.IMREAD_GRAYSCALE), None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA),
    "next_battle": cv2.resize(cv2.imread("src/next_battle.png", cv2.IMREAD_GRAYSCALE), None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA),
    "end_battle": cv2.resize(cv2.imread("src/end_battle.png", cv2.IMREAD_GRAYSCALE), None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA),
}

region = (left, top, region_width, region_height) 
threshold = 0.75  

def detect_windows():
    global posRecent, count
    screenshot = pyautogui.screenshot(region=region)
    screenshot = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    small_screenshot = cv2.resize(screenshot_gray, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)

    # Recorrer cada tipo de ventana y sus plantillas (listas de imágenes o una sola imagen)
    for window_type, templates_list in templates.items():
        # Si templates_list es una lista, iteramos sobre cada imagen en esa lista
        if isinstance(templates_list, list):
            for template in templates_list:
                result = cv2.matchTemplate(small_screenshot, template, cv2.TM_CCOEFF_NORMED)
                loc = np.where(result >= threshold)

                # Si encontramos una coincidencia, ejecutamos la acción para "inicio"
                if len(loc[0]) > 0:
                    if window_type == "inicio":
                        if posRecent == posReward or posRecent == -1 or posRecent == posEndBattle:
                            count = 0
                            posRecent = posInicio
                            time.sleep(tiempo_antes_de_la_accion)
                            keyboard.press_and_release('a')
                            time.sleep(tiempo_despues_de_accion)
                            show_message_func("Acción: Iniciar juego.")
                    # Salir de la función después de detectar y ejecutar la acción
                    return

        # Si templates_list es una sola imagen, realizamos la detección sin bucle adicional
        else:
            result = cv2.matchTemplate(small_screenshot, templates_list, cv2.TM_CCOEFF_NORMED)
            loc = np.where(result >= threshold)

            if len(loc[0]) > 0:
                # Acciones para otros tipos de ventanas según el tipo detectado
                if window_type == "recompensa":
                    if posRecent == posEndBattle:
                        count = 0
                        posRecent = posReward
                        time.sleep(tiempo_antes_de_la_accion)
                        show_message_func("Acción: Recoger recompensa.")
                        time.sleep(tiempo_despues_de_accion)
                        keyboard.press_and_release('esc')
                elif window_type == "life":
                    if posRecent == posInicio:    
                        count = 0
                        posRecent = posLife
                        time.sleep(tiempo_antes_de_la_accion)
                        keyboard.press_and_release('r')
                        time.sleep(tiempo_despues_de_accion)
                        show_message_func("Acción: Curar.")
                    elif posRecent == posLife:
                        count = 0
                        posRecent = posAttack
                        time.sleep(tiempo_antes_de_la_accion)
                        keyboard.press_and_release('b')
                        time.sleep(tiempo_despues_de_accion)
                        show_message_func("Acción: Atacar.")
                elif window_type == "next_battle":
                    if posRecent == posAttack:
                        count = 0
                        posRecent = posNextBattle
                        show_message_func("Acción: siguiente batalla.")
                        time.sleep(tiempo_antes_de_la_accion)
                        keyboard.press_and_release('b')
                        time.sleep(tiempo_despues_de_accion)
                elif window_type == "end_battle":
                    if posRecent == posAttack or posRecent == posNextBattle:
                        count = 0
                        posRecent = posEndBattle
                        time.sleep(tiempo_antes_de_la_accion)
                        keyboard.press_and_release('esc')
                        time.sleep(tiempo_despues_de_accion)
                        show_message_func("Acción: Fin de la batalla.")
                else:
                    show_message_func("Ventana desconocida.")
                return

def start_detection(show_message):
    global program_running, count, posRecent, show_message_func
    program_running = True
    count = 0
    posRecent = -1
    show_message_func = show_message
    if show_message_func:
        show_message_func("Iniciando la detección de ventanas...")

    while program_running:
        count += 1
        if count > 15:
            time.sleep(tiempo_entre_cada_captura)
            keyboard.press_and_release('esc')
            time.sleep(tiempo_entre_cada_captura)
            count = 0
            posRecent = -1
            if show_message_func:
                show_message_func("Reiniciado")
        detect_windows()
        time.sleep(tiempo_entre_cada_captura)

def stop_detection():
    global program_running
    program_running = False
    if show_message_func:
        show_message_func("Deteniendo la detección de ventanas.")