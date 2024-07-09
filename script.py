import pandas as pd
from collections import Counter

# Lee el archivo .txt
file_path = 'text.txt'
with open(file_path, 'r') as file:
    parrafos = file.readlines()

# Une todos los párrafos en un solo texto
texto_completo = ' '.join(parrafos)

# Cuenta el número de caracteres
num_caracteres = len(texto_completo)
palabras = texto_completo.split()
# Cuenta el número de palabras
num_palabras = len(palabras)

# Cuenta la frecuencia de cada palabra
frecuencia_palabras = Counter(palabras)
# Convierte el contador a un DataFrame y ordena por frecuencia
df_frecuencia = pd.DataFrame(frecuencia_palabras.items(), columns=['Palabra', 'Frecuencia'])
df_frecuencia = df_frecuencia.sort_values(by='Frecuencia', ascending=False).reset_index(drop=True)

print(f"{num_caracteres} characters")
print(f"{num_palabras} words")
for index, row in df_frecuencia.iterrows():
    palabra = row['Palabra']
    frecuencia = row['Frecuencia']
    print(f"{palabra}: {frecuencia}")