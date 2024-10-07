import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, KBinsDiscretizer, StandardScaler

# Leer el archivo CSV completo en un DataFrame
file_path = 'c:/Users/oHm/Desktop/inf-354/examen1/pregunta2/electricityCSV.csv'
df = pd.read_csv(file_path, delimiter=';')


#  no tengo columnas categóricas, 
# encoder = OneHotEncoder(sparse=False)
# encoded_data = encoder.fit_transform(df[['Oil and Gas']])
# encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(['Oil and Gas']))
# df = pd.concat([df, encoded_df], axis=1)


# no tengo columnas categóricas, 
# label_encoder = LabelEncoder()
# df['Biomass_encoded'] = label_encoder.fit_transform(df['Biomass'])

# Discretización
discretizer = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='uniform')
df[['Consumption', 'Production', 'Nuclear', 'Wind', 'Hydroelectric', 'Oil and Gas', 'Coal', 'Solar', 'Biomass']] = discretizer.fit_transform(df[['Consumption', 'Production', 'Nuclear', 'Wind', 'Hydroelectric', 'Oil and Gas', 'Coal', 'Solar', 'Biomass']])

print(df)
# Guardar el DataFrame transformado en un archivo CSV
df.to_csv('datos_transformados_discretizado.csv', index=False)


# Normalización
scaler = StandardScaler()
df[['Consumption', 'Production', 'Nuclear', 'Wind', 'Hydroelectric', 'Oil and Gas', 'Coal', 'Solar', 'Biomass']] = scaler.fit_transform(df[['Consumption', 'Production', 'Nuclear', 'Wind', 'Hydroelectric', 'Oil and Gas', 'Coal', 'Solar', 'Biomass']])

print(df)

# Guardar el DataFrame transformado en un archivo CSV
df.to_csv('datos_transformados_normalizado.csv', index=False)

