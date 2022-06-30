import numpy as np
import pandas as pd
import random
import io

from google.colab import files 
uploaded = files.upload()
#cargamos un csv del disco a colab

ecomex= pd.read_csv(io.BytesIO(uploaded["ecomex.csv"]))
#Leemos el archivo con pd.read_csv

sample8 = ecomex.sample(n=8)
#Muestreo aleatorio simple de 8 elementos

sample8_2= ecomex.sample(n=8)
# Otra seleccion aleatoria

prop25 = ecomex.sample (frac=.25)
#seleccion aleatoria del 25% de los casos de la tabla

def systematic_sampling(ecomex, step):
  index=np.arange(0,len(ecomex),step=step)
  systematic_sample= ecomex.iloc[index]
  return systematic_sample
#funcion que nos genera un muestreo sistematico.

ecomex ["strat"] = ecomex ["delegacion"] + "," + ecomex ["tipo"]
(ecomex ["strat"].value_counts()/len(ecomex)).sort_values(ascending=False)
# Muestreo estratificado

def data_estratificada(ecomex, nombres_columnas_estrat, valores_estrat, prop_estrat, random_state=None):
    
    df_estrat = pd.DataFrame(columns = ecomex.columns) # Creamos un data frame vacío con los nombres de las columnas de econdata

    pos = -1
    for i in range(len(valores_estrat)): # iteración sobre los valores estratificados
        pos += 1
        if pos == len(valores_estrat) - 1: 
            ratio_len = len(ecomex) - len(df_estrat) # si es la iteración final calcula el número de valores de salida tenga el mismo número 
                                                       # de filas que de entrada
        else:
            ratio_len = int(len(ecomex) * prop_estrat[i]) # calcula el número de filas según la proporción deseada

        df_filtrado = ecomex[ecomex[nombres_columnas_estrat] ==valores_estrat[i]] # filtra los datos de origen según los valores seleccionados 
                                                                                      # en la estratificación de datos
        
        df_temp = df_filtrado.sample(replace=True, n=ratio_len, random_state=random_state) # haz un sample de los datos filtrados usando la ratio 
                                                                                           # que hemos calculado
        
        df_estrat = pd.concat([df_estrat, df_temp]) # junta las tablas de sample con la estratificada para producir el resultado final
        
    return df_estrat # Return the stratified, re-sampled data

valores_estrat = ['Cuautémoc,Hotel', 'Cuautémoc,Museo', 'Venustiano Carranza,Hotel', 'Cuauhtémoc,Mercado','Venustiano Carranza,Mercado']
prop_estrat = [0.5, 0.2, 0.1, 0.1,0.1]
df_estrat = data_estratificada(ecomex, 'estratificado', valores_estrat, prop_estrat, random_state=42)
df_estrat