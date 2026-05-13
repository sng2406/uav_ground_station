# UAV Ground Station Simulator

Basic UAV telemetry simulator developed in Python with a graphical interface using Tkinter.

This project was created to learn and demonstrate fundamental concepts related to UAV systems, avionics telemetry, real-time GUI updates, and basic system state management.

---

# Features

- Real-time UAV telemetry simulation
- Randomized flight parameters
- Roll / Pitch / Yaw simulation
- Battery consumption simulation
- Low battery warning system
- UAV shutdown state
- Graphical User Interface (GUI)
- Real-time terminal logging
- Event-driven update system using Tkinter

---

# Simulated Telemetry

The simulator generates and updates:

- Altitude
- Speed
- Roll
- Pitch
- Yaw
- Battery percentage

---

# Technologies Used

- Python 3
- Tkinter
- Random module
- Event-driven GUI architecture

---

# GUI Preview

The GUI displays simulated telemetry values in real time and includes warning states for:

- Low battery
- UAV battery depletion

---


# How It Works

The application uses:

- Tkinter for the graphical interface
- root.after() for periodic real-time updates
- Randomized telemetry generation to simulate UAV flight data
- Label widgets dynamically updated using .config()

The system continuously updates telemetry values until the battery reaches 0%.

Example Telemetry
```
Altitude: 123 m
Speed: 35 m/s
Roll: -2.31 °
Pitch: 1.22 °
Yaw: 182.51 °
Battery: 84.3 %
```
# How  to run
To execute this program run the following command in the current directory:
```
python ./simulator_interfaz.py
```
