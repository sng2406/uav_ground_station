# ==========================
# UAV TELEMETRY SIMULATOR
# ==========================

# Librería para crear la interfaz gráfica de usuario (GUI) del simulador
import tkinter as tk 
# libreria randomizada para simular cambios en la telemetría del UAV en tiempo real 
import random
# libreria time para simular un retraso entre cada actualización de telemetría
import time 

# ==========================
# INITIAL UAV STATE
# ==========================

# Batería inicial del UAV
battery = 100

# ==========================
# MAIN LOOP
# ==========================

while battery > 0:

    # Altitud del UAV en metros
    altitude = random.randint(100,130)  # Simula una altitud entre 100 y 130 metros 

    # Velocidad en metros por segundo
    speed = random.randint(20,40)  # Simula una velocidad entre 30 y 40 metros por segundo numeros decimales

    # Inclinación lateral del UAV
    roll = round(random.uniform(-10, 10), 2)  # Simula una inclinación lateral entre -10 y 10 grados numeros decimales, redondea a 2 decimales

    # Inclinación frontal del UAV
    pitch = round(random.uniform(-5, 5), 2) # Simula una inclinación frontal entre -5 y 5 grados numeros decimales, redondea a 2 decimales

    # Orientación/brújula del UAV
    yaw = round(random.uniform(0, 359.9), 2)  # Simula una orientación entre 0 y 359.9 grados numeros decimales, redondea a 2 decimales

    # Porcentaje de batería restante
    battery = max(0, round(battery - random.uniform(0.1, 0.5), 2))  # Simula un consumo de batería entre 0.1% y 0.5% por actualización, no permite que baje de 0%

    # ==========================
    # TELEMETRY OUTPUT
    # ==========================

    print("\n====================")
    print("UAV TELEMETRY")
    print("====================")

    print("\nAltitude:", altitude, "m")
    print("Speed:", speed, "m/s")
    print("Roll:", roll, "°")
    print("Pitch:", pitch, "°")
    print("Yaw:", yaw, "°")
    print("Battery:", battery, "%")

    root = tk.Tk()
root.title("Telemetría UAV")

# Etiquetas para cada variable
label_altitude = tk.Label(root, text="Altitude: 0 m")
label_altitude.pack()

label_speed = tk.Label(root, text="Speed: 0 m/s")
label_speed.pack()

label_roll = tk.Label(root, text="Roll: 0°")
label_roll.pack()

label_pitch = tk.Label(root, text="Pitch: 0°")
label_pitch.pack()

label_yaw = tk.Label(root, text="Yaw: 0°")
label_yaw.pack()

label_battery = tk.Label(root, text="Battery: 100%")
label_battery.pack()

# Inicia la actualización
root.after(1000, actualizar)

# Inicia la interfaz gráfica
root.mainloop()

    # Esperar 1 segundo
time.sleep(1)
print("\nUAV has run out of battery. Simulation ended.")

