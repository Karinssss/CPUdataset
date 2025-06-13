import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# URL del archivo CSV en GitHub (RAW)
url = "https://raw.githubusercontent.com/Karinssss/CPUdataset/main/procesos_20250613_092952.csv"

# Cargar el dataset desde GitHub
df = pd.read_csv(url)

# Asegurar tipos numéricos
df["cpu_percent"] = pd.to_numeric(df["cpu_percent"], errors="coerce")
df["memory_percent"] = pd.to_numeric(df["memory_percent"], errors="coerce")

# Eliminar filas con NaN en columnas numéricas
df.dropna(subset=["cpu_percent", "memory_percent"], inplace=True)

# Estadísticas básicas
print("📊 Estadísticas Básicas:")
print("Media:")
print(df[["cpu_percent", "memory_percent"]].mean())

print("\nMediana:")
print(df[["cpu_percent", "memory_percent"]].median())

print("\nModa:")
print(df[["cpu_percent", "memory_percent"]].mode().iloc[0])

print("\nDesviación Estándar:")
print(df[["cpu_percent", "memory_percent"]].std())

# Matriz de correlación
print("\n📈 Matriz de Correlación:")
print(df[["cpu_percent", "memory_percent"]].corr())

# Visualización opcional
sns.heatmap(df[["cpu_percent", "memory_percent"]].corr(), annot=True, cmap="coolwarm")
plt.title("Matriz de Correlación entre CPU y RAM")
plt.show()
