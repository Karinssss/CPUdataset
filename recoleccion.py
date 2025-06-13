import psutil
import pandas as pd
import time
from datetime import datetime
import os

# Inicializar CPU para los procesos
for p in psutil.process_iter(['pid', 'name']):
    try:
        p.cpu_percent(interval=None)
    except psutil.NoSuchProcess:
        continue

time.sleep(1)  # Espera para que los valores de CPU sean reales

# Recolectar procesos
procesos = []
for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
    try:
        procesos.append(p.info)
    except psutil.NoSuchProcess:
        continue

# Crear DataFrame
df = pd.DataFrame(procesos)

# Crear nombre de archivo y ruta completa
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
nombre_archivo = f"procesos_{timestamp}.csv"
ruta_destino = os.path.join("parcial2", nombre_archivo)

# Asegurarse de que la carpeta exista
os.makedirs("parcial2", exist_ok=True)

# Guardar archivo
df.to_csv(ruta_destino, index=False)

print(f"✅ Dataset guardado en: {ruta_destino}")
