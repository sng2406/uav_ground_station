import tkinter as tk # Librería para crear la interfaz gráfica de usuario (GUI) del simulador
import random # libreria para simular cambios en la telemetría del UAV en tiempo real

# ==========================
# INITIAL UAV STATE
# ==========================

battery = 100 # Batería inicial del UAV

# ==========================
# TKINTER WINDOW
# ==========================

root = tk.Tk() # Crea la ventana principal de la interfaz gráfica de usuario (GUI) del simulador

root.title("UAV TELEMETRY") # Establece el título de la ventana como "UAV TELEMETRY"

root.geometry("300x150") # Establece el tamaño de la ventana a 300 píxeles de ancho y 150 píxeles de alto

# ==========================
# LABELS
# ==========================

label_altitude = tk.Label(root, text="Altitude: ") # nombre de Label, comdando de label, destino ventana principal, tipo de objeto, "contenido del objeto"
label_altitude.pack() # Empaqueta el label en la ventana para que se muestre

label_speed = tk.Label(root, text="Speed: ") # Label para mostrar la velocidad del UAV
label_speed.pack() # Empaqueta el label en la ventana para que se muestre

label_roll = tk.Label(root, text="Roll: ") # Label para mostrar la inclinación lateral del UAV
label_roll.pack() # Empaqueta el label en la ventana para que se muestre

label_pitch = tk.Label(root, text="Pitch: ") # Label para mostrar la inclinación frontal del UAV
label_pitch.pack() # Empaqueta el label en la ventana para que se muestre

label_yaw = tk.Label(root, text="Yaw: ") # Label para mostrar la orientación del UAV
label_yaw.pack() # Empaqueta el label en la ventana para que se muestre

label_battery = tk.Label(root, text="Battery: ") # Label para mostrar el porcentaje de batería restante
label_battery.pack() # Empaqueta el label en la ventana para que se muestre

label_lowbattery = tk.Label(root, text="", fg="red") # Label para mostrar advertencia de batería baja
label_lowbattery.pack() # Empaqueta el label en la ventana para que se muestre

label_nobattery = tk.Label(root, text="", fg="red") # Label para mostrar advertencia de batería agotada
label_nobattery.pack() # Empaqueta el label en la ventana para que se muestre
# ==========================
# UPDATE FUNCTION
# ==========================

def actualizar(): # Función para actualizar la telemetría del UAV y mostrarla en la terminal y en la GUI

    global battery # Indica que se va a modificar la variable global "battery" dentro de esta función

    # Altitud del UAV
    altitude = random.randint(100, 130) # Simula una altitud entre 100 y 130 metros

    # Velocidad del UAV
    speed = random.randint(20, 40) # Simula una velocidad entre 20 y 40 metros por segundo

    # Roll
    roll = round(random.uniform(-10, 10), 2) # Simula una inclinación lateral entre -10 y 10 grados numeros decimales, redondea a 2 decimales

    # Pitch
    pitch = round(random.uniform(-5, 5), 2) # Simula una inclinación frontal entre -5 y 5 grados numeros decimales, redondea a 2 decimales

    # Yaw
    yaw = round(random.uniform(0, 359.9), 2) # Simula una orientación entre 0 y 359.9 grados numeros decimales, redondea a 2 decimales

    # Consumo batería
    battery = max(0, round(battery - random.uniform(0.1, 0.5), 2)) # Asegura que la batería no sea negativa, simula un consumo de batería entre 0.1% y 0.5% por actualización, redondea a 2 decimales

    # ==========================
    # TERMINAL OUTPUT
    # ==========================

    print("\n====================")
    print("UAV TELEMETRY")
    print("====================")

    print("Altitude:", altitude, "m")
    print("Speed:", speed, "m/s")
    print("Roll:", roll, "°")
    print("Pitch:", pitch, "°")
    print("Yaw:", yaw, "°")
    print("Battery:", battery, "%")

    # ==========================
    # GUI OUTPUT
    # ==========================

    label_altitude.config(text=f"Altitude: {altitude} m") # Actualiza el texto del label de altitud con el valor simulado

    label_speed.config(text=f"Speed: {speed} m/s") # Actualiza el texto del label de velocidad con el valor simulado

    label_roll.config(text=f"Roll: {roll} °") # Actualiza el texto del label de roll con el valor simulado

    label_pitch.config(text=f"Pitch: {pitch} °") # Actualiza el texto del label de pitch con el valor simulado

    label_yaw.config(text=f"Yaw: {yaw} °") # Actualiza el texto del label de yaw con el valor simulado

    label_battery.config(text=f"Battery: {battery} %") # Actualiza el texto del label de batería con el valor simulado

    # LOW BATTERY WARNING

    if battery < 20:

        label_lowbattery.config(text="LOW BATTERY WARNING", fg="red")
        print("LOW BATTERY WARNING")
    # Repeat every 1 second

    if battery > 0:

        root.after(1000, actualizar)

    else:
        label_lowbattery.pack_forget()
        label_nobattery.config(text="UAV HAS RUN OUT OF BATTERY", fg="red")
        print("\nUAV HAS RUN OUT OF BATTERY")# ==========================
# START SYSTEM
# ==========================

actualizar()

# ==========================
# TKINTER MAIN LOOP
# ==========================

root.mainloop()