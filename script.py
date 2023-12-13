import pandas as pd
import pickle
from sqlalchemy import create_engine


# Establecer la conexión a la base de datos
nombre_de_usuario = 'user'
contraseña = 'password'
nombre_de_base_de_datos = 'imserso_database'
nombre_de_host = 'localhost'  # O el host de tu base de datos
puerto = '3306'  # El puerto de tu base de datos MySQL

# Cadena de conexión para MySQL
cadena_conexion = f"mysql+pymysql://{nombre_de_usuario}:{contraseña}@{nombre_de_host}:{puerto}/{nombre_de_base_de_datos}"

# Crear el motor de la base de datos
engine = create_engine(cadena_conexion)

# Cargar todos los DataFrame desde el archivo pickle de cada script de python
with open('df_bbdd.pickle', 'rb') as f:
    df_bbdd = pickle.load(f)

with open('df_esperanza_vida.pickle', 'rb') as f:
    df_bbdd = pickle.load(f)

with open('df_proximo_viaje.pickle', 'rb') as f:
    df_bbdd = pickle.load(f)

with open('df_tipos_viaje.pickle', 'rb') as f:
    df_bbdd = pickle.load(f)

# Insertar el DataFrame df_bbdd en la tabla de la base de datos (PERO ESTO NO FUNCIONA)
df_bbdd.to_sql('Tipo_de_viaje', con=engine, if_exists='append', index=False)

# Cierra la conexión después de realizar la inserción
engine.dispose()
