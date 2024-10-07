import pandas as pd
from sklearn.linear_model import LinearRegression

# Cargar el archivo CSV normalizado
df = pd.read_csv(r'C:\Users\oHm\Desktop\inf-354\examen1\pregunta5\datos_transformados_normalizados.csv')

# Separar las características (X) y la variable objetivo (y)
# Supongamos que 'Consumption' es la variable objetivo
X = df[['Production', 'Nuclear', 'Wind', 'Hydroelectric', 'Oil and Gas', 'Coal', 'Solar', 'Biomass']]
y = df['Consumption']




# Entrenar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X, y)

# Obtener los coeficientes del modelo
coeficientes = modelo.coef_
nombres_columnas = X.columns

# Crear un diccionario de coeficientes
coeficientes_dict = dict(zip(nombres_columnas, coeficientes))

print("Coeficientes del modelo:", coeficientes_dict)



# Función para calcular la penalización L1
def penalizacion_l1(coeficientes, alpha):
    return alpha * sum(abs(c) for c in coeficientes.values())

# Función para calcular la penalización L2
def penalizacion_l2(coeficientes, alpha):
    return alpha * sum(c**2 for c in coeficientes.values())

# Parámetro de regularización
alpha = 0.1

# Calcular las penalizaciones
penalizacion_l1_valor = penalizacion_l1(coeficientes_dict, alpha)
penalizacion_l2_valor = penalizacion_l2(coeficientes_dict, alpha)

print("Penalización L1:", penalizacion_l1_valor)
print("Penalización L2:", penalizacion_l2_valor)
