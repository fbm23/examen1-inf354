import csv
import matplotlib.pyplot as plt

#calcula los percentiles
def calculate_percentiles(data, percentiles):
    sorted_data = sorted(data)
    n = len(sorted_data)
    results = {}
    for p in percentiles:
        k = (n - 1) * (p / 100)
        f = int(k)
        c = k - f
        if f + 1 < n:
            results[p] = sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
        else:
            results[p] = sorted_data[f]
    return results

#calcula los cuartiles
def calculate_quartiles(data):
    return calculate_percentiles(data, [25, 50, 75])

#lee la columna del csv
def read_column_from_csv(file_path, column_name):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            if column_name in row:
                data.append(float(row[column_name]))
    return data

#grafica los datos por columna
def plot_data(data, title, xlabel):
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=20, alpha=0.7, color='blue', edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Frecuencia (dia)')
    plt.grid(True)
    plt.show()

# Ruta al archivo CSV
file_path = 'c:/Users/oHm/Desktop/inf-354/examen1/pregunta2/electricityCSV.csv'

print("----------------------------------------------")
# analisis de consumo de electricidad
print("Consumo de electricidad")
data = read_column_from_csv(file_path, 'Consumption')
percentiles = calculate_percentiles(data, [ 10, 30, 50, 70, 90])
quartiles = calculate_quartiles(data)

print("Percentiles:", percentiles)
print("Cuartiles:", quartiles)
# grafica del consumo de electricidad
plot_data(data, 'Distribución de Consumo de Electricidad', 'Consumo (MWs/dia)')

print("----------------------------------------------")
# analisis de la produccion total de electricidad
print("Producción de electricidad")
data = read_column_from_csv(file_path, 'Production')
percentiles = calculate_percentiles(data, [ 10, 30, 50, 70, 90])
quartiles = calculate_quartiles(data)

print("Percentiles:", percentiles)
print("Cuartiles:", quartiles)
# grafica de la produccion de electricidad
plot_data(data, 'Distribución de Producción de Electricidad', 'Producción (MWs/dia)')

print("----------------------------------------------")
# analisis de la produccion de energia Nuclear
print("Producción de energia Nuclear")
data = read_column_from_csv(file_path, 'Nuclear')
percentiles = calculate_percentiles(data, [ 10, 30, 50, 70, 90])
quartiles = calculate_quartiles(data)

print("Percentiles:", percentiles)
print("Cuartiles:", quartiles)
# grafica de la produccion de energia Nuclear
plot_data(data, 'Distribución de Producción de Energía Nuclear', 'Producción Energia Nuclear (MWs/dia)')

print("----------------------------------------------")
# analisis de la produccion de energia eólica
print("Producción de energia Eólica")
data = read_column_from_csv(file_path, 'Wind')
percentiles = calculate_percentiles(data, [ 10, 30, 50, 70, 90])
quartiles = calculate_quartiles(data)

print("Percentiles:", percentiles)
print("Cuartiles:", quartiles)
# grafica de la produccion de energia eólica
plot_data(data, 'Distribución de Producción de Energía Eólica', 'Producción Energia Eólica (MWs/dia)')

print("----------------------------------------------")
# analisis de la produccion de energia hidroeléctrica
print("Producción de energia Hidroeléctrica")
data = read_column_from_csv(file_path, 'Hydroelectric')
percentiles = calculate_percentiles(data, [ 10, 30, 50, 70, 90])
quartiles = calculate_quartiles(data)

print("Percentiles:", percentiles)
print("Cuartiles:", quartiles)
# grafica de la produccion de energia hidroeléctrica
plot_data(data, 'Distribución de Producción de Energía Hidroeléctrica', 'Producción Energia Hidroeléctrica (MWs/dia)')

print("----------------------------------------------")
# analisis de la produccion de energia de petróleo y gas
print("Producción de energia de petróleo y gas")
data = read_column_from_csv(file_path, 'Oil and Gas')
percentiles = calculate_percentiles(data, [ 10, 30, 50, 70, 90])
quartiles = calculate_quartiles(data)

print("Percentiles:", percentiles)
print("Cuartiles:", quartiles)
# grafica de la produccion de energia de petróleo y gas
plot_data(data, 'Distribución de Producción de Energía de Petróleo y Gas', 'Producción Energia Petróleo y Gas (MWs/dia)')

print("----------------------------------------------")
# analisis de la produccion de energia de carbón
print("Producción de energia de carbón")
data = read_column_from_csv(file_path, 'Coal')
percentiles = calculate_percentiles(data, [ 10, 30, 50, 70, 90])
quartiles = calculate_quartiles(data)

print("Percentiles:", percentiles)
print("Cuartiles:", quartiles)
# grafica de la produccion de energia de carbón
plot_data(data, 'Distribución de Producción de Energía de Carbón', 'Producción Energia Carbón (MWs/dia)')

print("----------------------------------------------")
# analisis de la produccion de energia solar
print("Producción de energia Solar")
data = read_column_from_csv(file_path, 'Solar')
percentiles = calculate_percentiles(data, [ 10, 30, 50, 70, 90])
quartiles = calculate_quartiles(data)

print("Percentiles:", percentiles)
print("Cuartiles:", quartiles)
# grafica de la produccion de energia solar
plot_data(data, 'Distribución de Producción de Energía Solar', 'Producción Energia Solar (MWs/dia)')

print("----------------------------------------------")
# analisis de la produccion de energia de biomasa
print("Producción de energia de biomasa")
data = read_column_from_csv(file_path, 'Biomass')
percentiles = calculate_percentiles(data, [ 10, 30, 50, 70, 90])
quartiles = calculate_quartiles(data)

print("Percentiles:", percentiles)
print("Cuartiles:", quartiles)
# grafica de la produccion de energia de biomasa
plot_data(data, 'Distribución de Producción de Energía de Biomasa', 'Producción Energia Biomasa (MWs/dia)')
