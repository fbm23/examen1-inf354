import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Leer el archivo CSV en un DataFrame
file_path = 'c:/Users/oHm/Desktop/inf-354/examen1/pregunta2/electricityCSV.csv'
df = pd.read_csv(file_path, delimiter=';')

# Seleccionar las columnas de interés
columns = ['Consumption', 'Production', 'Nuclear', 'Hydroelectric', 'Solar']

# Calcular estadísticas
for column in columns:
    media = df[column].mean()
    mediana = df[column].median()
    moda = df[column].mode()[0]
    print(f"{column} - Media: {media}, Mediana: {mediana}, Moda: {moda}")

# Graficar el diagrama de cajas y bigotes
plt.figure(figsize=(10, 6))
df[columns].boxplot()
plt.title('Diagrama de Cajas y Bigotes')
plt.ylabel('Valores')
plt.grid(True)
plt.show()