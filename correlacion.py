import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.datasets import breast_cancer

breast_camcer= load_breast_cancer()
data= breast_camcer.data
# la variable "data" recibe como valor los datos del data frame.

features= breast_camcer.features
# la variable "features" recibe como valor los nombres de las columnas.

df= pd.DataFrame(data, columns=features)
# .DataFrame() nos permite crear un nuevo df
# columns= nos permite asignar los nombre de las columnas.

df_short= df.iloc[:,:6]
# .iloc[] nos pemrmite trabajar con los df como si fueran listas y seleccionar por filas y columnas.
# en este caso estamos seleccionando todas las filas pero solo seis columnas.

df_short.corr()
# nos arroja una tabla con las correlaciones de las variables que tenemos en nuestro df.

corr_mat = df_short.corr()

sns.heatmap(corr_mat, annot=True)
# annot= añade al grafico los valores de correlacion
plt.show

corr_mat.unstack()
# .unstack() desagrega la matriz de correlacion y la pone en dos columnas (un vector).

corr_val= corr_mat.unstack()

corr_val.sort_values(kind= "quicksort")
# .sort_values() nos ordena los valores de nuestro vector

sns.pairplot(df_short)
# .pairplot() nos da el grafico de todas las correlaciones.

