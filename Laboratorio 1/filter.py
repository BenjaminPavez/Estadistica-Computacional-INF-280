# -----------------------------------------------------------------------------
#
# Filtrado de datos para la visualización de gráficos de barras
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
# El siguiente script realiza un filtrado de datos para obtener los FPS promedio 
# dado una CPU, resolución y juego específico.
#
# -----------------------------------------------------------------------------

import pandas as pd


#Confiuracion de los parametros
cpu = "AMD Ryzen 5 2600"
juego = "leagueOfLegends"
resolucion = 1080

#Dataset
df = pd.read_csv("DataGraficos.csv")

game_data = df[(df['GameName'] == juego) & (df['CpuName'] == cpu) & (df['GameResolution'] == resolucion)]


grouped_data = game_data.groupby('GpuName')

#Calcula el punto medio o el promedio de los FPS para cada combinación de GPU
result = grouped_data['FPS'].mean().reset_index()

# Define las categorías de ajuste
game_settings = ['low', 'med', 'high', 'max']

print("--------------------------------------------------")
print("CPU:", cpu)
print("Game:", game_data['GameName'].iloc[0])
print("Resolution:", game_data['GameResolution'].iloc[0])
print("--------------------------------------------------")
print()


for gpu in result['GpuName']:
    print("--------------------------------------------------")
    print("GPU:", gpu)
    gpu_data = game_data[(game_data['GpuName'] == gpu)]
    for setting in game_settings:
        fps_value = gpu_data[gpu_data['GameSetting'] == setting]['FPS'].mean()
        if pd.notnull(fps_value):
            print(f"{setting}: {round(fps_value,1)} FPS")
        else:
            print(f"{setting}: None")
    print("--------------------------------------------------")
    print()