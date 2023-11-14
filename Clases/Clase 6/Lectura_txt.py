
import pandas as pd
### Lectura del archivo .txt
df = pd.read_csv(r"C:\Users\sanch\OneDrive\Documentos\GitHub\Data-Engineering---CoderHouse\Clases\Clase 6\pokemon_data.txt", delimiter="\t")
# Mostrar las ultimas 10 filas 
df.tail(10)
print(df.shape)
print(df.columns)
#Mostrar columnas "name", "type 1", "Attack", "Defense"
print(df[["Name", "Type 1", "Attack", "Defense"]].head())