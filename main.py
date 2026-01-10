import tkinter as tk
from datetime import datetime
import subprocess
import wmi
import win32com.client

# -----------------------------
# WMI inicializace
# -----------------------------
w = wmi.WMI(namespace="root\\wmi")

# -----------------------------
# Čtení teplot
# -----------------------------

def get_temperatures():
    cpu_temp = 0
    gpu_temp = 0

    try:
        wmi = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        service = wmi.ConnectServer(".", "root\\OpenHardwareMonitor")

        sensors = service.ExecQuery("SELECT * FROM Sensor")
        for sensor in sensors:
            if sensor.SensorType == u'Temperature':
                if 'CPU' in sensor.Name and cpu_temp == 0:
                    cpu_temp = float(sensor.Value)
                if 'GPU' in sensor.Name:
                    gpu_temp = float(sensor.Value)
    except Exception:
        pass
    return cpu_temp, gpu_temp

# -----------------------------
# Barva podle teploty
# -----------------------------
def temp_color(temp, max_safe):
    if temp < max_safe * 0.7:
        return "lime"
    elif temp < max_safe * 0.9:
        return "orange"
    else:
        return "red"

# -----------------------------
# Aktualizace GUI
# -----------------------------
def update():
    cpu, gpu = get_temperatures()
    now = datetime.now()

    label_time.config(text=now.strftime("%H:%M:%S"))
    label_date.config(text=now.strftime("%d.%m.%Y"))

    # CPU
    canvas_cpu.delete("all")
    canvas_cpu.create_oval(10, 10, 150, 150, outline="#333", width=15)
    canvas_cpu.create_arc(
        10, 10, 150, 150,
        start=90, extent=-min(cpu, 100) * 2.7,
        style="arc", width=15,
        outline=temp_color(cpu, 80)
    )
    canvas_cpu.create_text(
        80, 80, text=f"{cpu:.1f}°C",
        fill=temp_color(cpu, 80),
        font=("Arial", 16, "bold")
    )
    canvas_cpu.create_text(80, 160, text="CPU", font=("Arial", 20, "bold"), fill="white")

    # GPU
    canvas_gpu.delete("all")
    canvas_gpu.create_oval(10, 10, 150, 150, outline="#333", width=15)
    canvas_gpu.create_arc(
        10, 10, 150, 150,
        start=90, extent=-min(gpu, 100) * 2.7,
        style="arc", width=15,
        outline=temp_color(gpu, 90)
    )
    canvas_gpu.create_text(
        80, 80, text=f"{gpu:.1f}°C",
        fill=temp_color(gpu, 90),
        font=("Arial", 16, "bold")
    )
    canvas_gpu.create_text(80, 160, text="GPU", font=("Arial", 20, "bold"), fill="white")

    root.after(1000, update)

# -----------------------------
# Fullscreen toggle
# -----------------------------
def toggle_fullscreen(event=None):
    global fullscreen
    fullscreen = not fullscreen
    root.attributes("-fullscreen", fullscreen)

# -----------------------------
# GUI
# -----------------------------
root = tk.Tk()
root.title("PC Monitoring Panel")
root.configure(bg="#1e1e1e")

# Fullscreen
fullscreen = True
root.attributes("-fullscreen", fullscreen)

# Ovládání
root.bind("<Escape>", lambda e: root.destroy())
root.bind("<F11>", toggle_fullscreen)

# Čas
label_time = tk.Label(
    root, text="", font=("DS-Digital", 48, "bold"),
    fg="white", bg="#1e1e1e"
)
label_time.pack(pady=(20, 0))

# Datum
label_date = tk.Label(
    root, text="", font=("DS-Digital", 24, "bold"),
    fg="white", bg="#1e1e1e"
)
label_date.pack(pady=(0, 20))

# Layout
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

canvas_cpu = tk.Canvas(frame, width=160, height=200, bg="#1e1e1e", highlightthickness=0)
canvas_cpu.pack(side="left", padx=50)

canvas_gpu = tk.Canvas(frame, width=160, height=200, bg="#1e1e1e", highlightthickness=0)
canvas_gpu.pack(side="right", padx=50)

update()
root.mainloop()
