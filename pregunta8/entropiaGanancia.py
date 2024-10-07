import pandas as pd
import numpy as np


# Crear el dataset
data = {
    'Altura': [170, 165, 180, 175, 160, 155, 190, 185, 150, 145, 175, 170, 165, 160, 155, 150, 145, 140, 135, 130],
    'Peso': [70, 65, 80, 75, 60, 55, 90, 85, 50, 45, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30],
    'Talla': ['M', 'M', 'L', 'L', 'S', 'S', 'XL', 'XL', 'S', 'S', 'L', 'M', 'M', 'S', 'S', 'S', 'S', 'S', 'S', 'S']
}

df = pd.DataFrame(data)

# Determinar la clase suponiendo que son deportistas o no
#  si la altura es mayor a 160 y el peso es mayor a 60, clasifico  como "Deportista"
df['Clase'] = df.apply(lambda row: 'Deportista' if row['Altura'] > 160 and row['Peso'] > 60 else 'No Deportista', axis=1)

print(df)



#calculo de la entropia 

def calcular_entropia(df, columna_clase):
    clases = df[columna_clase].unique()
    entropia = 0
    for clase in clases:
        p = len(df[df[columna_clase] == clase]) / len(df)
        entropia -= p * np.log2(p)
    return entropia

entropia_total = calcular_entropia(df, 'Clase')

print("Entropía total:", entropia_total)

#calculo de la ganancia
def calcular_ganancia_informacion(df, columna_caracteristica, columna_clase):
    valores_caracteristica = df[columna_caracteristica].unique()
    entropia_condicional = 0
    for valor in valores_caracteristica:
        sub_df = df[df[columna_caracteristica] == valor]
        p = len(sub_df) / len(df)
        entropia_condicional += p * calcular_entropia(sub_df, columna_clase)
    ganancia_informacion = entropia_total - entropia_condicional
    return ganancia_informacion

ganancia_altura = calcular_ganancia_informacion(df, 'Altura', 'Clase')
ganancia_peso = calcular_ganancia_informacion(df, 'Peso', 'Clase')
ganancia_talla = calcular_ganancia_informacion(df, 'Talla', 'Clase')

print("Ganancia de información (Altura):", ganancia_altura)
print("Ganancia de información (Peso):", ganancia_peso)
print("Ganancia de información (Talla):", ganancia_talla)
