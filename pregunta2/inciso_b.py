import matplotlib.pyplot as plt
import csv
from datetime import datetime

# leer columna del csv
def read_column_from_csv(file_path, column_name):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            if column_name in row:
                if column_name == 'DateTime':
                    data.append(row[column_name])  # Mantener como cadena
                else:
                    data.append(float(row[column_name]))  # Convertir a float solo si es numérico
    return data

# Gráfico de Dispersión entre el consumo y la producción de electricidad
def plot_dispercion(x_data, y_data, x_label, y_label, title):
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, alpha=0.7, edgecolors='w', s=100, c='blue', label='Producción')
    plt.scatter(y_data, x_data, alpha=0.7, edgecolors='w', s=100, c='red', label='Consumo')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(True)
    plt.show()

# grafico de la producion solar en funcion del tiempo
def plot_solar_scatter(date_times, solar_data):
    # Convertir las fechas a objetos datetime
    date_times = list(map(lambda x: datetime.strptime(x, '%d/%m/%Y %H:%M'), date_times))
    
    plt.figure(figsize=(12, 6))
    plt.scatter(date_times, solar_data, alpha=0.7, edgecolors='w', s=50, c='orange')
    plt.title('Dispersión de Energía Solar en Función del Tiempo')
    plt.xlabel('Fecha y Hora')
    plt.ylabel('Producción Solar (MWs)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Ruta al archivo CSV
file_path = 'c:/Users/oHm/Desktop/inf-354/examen1/pregunta2/electricityCSV.csv'

print("--------------------- dispercion----------------------------")
consumption_data = read_column_from_csv(file_path, 'Consumption')
production_data = read_column_from_csv(file_path, 'Production')

plot_dispercion(consumption_data, production_data, 'Consumo', 'Producción', 'Consumo vs Producción')

print("---------------------mapa calor energia solar------------------------------")

date_times = read_column_from_csv(file_path, 'DateTime')
solar_data = read_column_from_csv(file_path, 'Solar')

# Graficar
plot_solar_scatter(date_times, solar_data)