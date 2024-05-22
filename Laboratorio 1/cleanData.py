# -----------------------------------------------------------------------------
#
# Limpieza del dataset
#
# Desarrollado por: Renato Ramirez
#                   Matias Torrejon
#                   Benjamin Pavez
#                   Diego Cisternas
#
# Fecha Inicio: 05-05-2024
#
# Fecha Ultima Modificacion: 05-05-2024
#
#
# Este código fuente representa una parte del proyecto de Estadistica Computacional
# (INF-280), para mas informacion revisar el README en GitHub.
#
# El código fuente se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; sin siquiera la garantía implícita de
# APTITUD PARA UN PROPÓSITO PARTICULAR.
#
#
# DESCRIPCIÓN:
# El siguiente script realiza una limpieza de datos en un archivo CSV.
#
# -----------------------------------------------------------------------------

import pandas as pd


df = pd.read_csv('1.csv') #EL ARCHIVO '1.csv' NO ESTA EN EL REPOSITORIO DEBIDO A QUE ES MUY GRANDE


columnas_a_mantener = ['id','CpuName', 'CpuNumberOfCores','CpuNumberOfThreads','CpuFrequency','GpuName','GpuMemorySize','GameResolution','GameSetting','GameName','FPS']
df = df[columnas_a_mantener]

df = pd.read_csv('nuevo_archivo.csv', low_memory=False, na_values="?")
df_cleaned = df.dropna()

#Guarda el DataFrame modificado en un nuevo archivo CSV
df_cleaned.to_csv('nuevo_archivo.csv', index=False)

print("Columnas eliminadas correctamente")