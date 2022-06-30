import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
# de la libreria sklearn nos trae un modo de entrenamiento de red neuronal.
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import classification_report,confusion_matrix
# nos permite crear reportes y matrices de confusion.

iris = datasets.load_iris

data= pd.DataFrame(iris.data)
# .Data solo nos carga los datos del dataset
data.columns= iris.feature_names
# .columns asigna nombres a las columnas 
# iris.feature_mames contiene los nombres de las columnas.


data.describe().transpose()
# .transpose() invierte el orden de las filas y las columnas

target_column = ['target','names'] 
#son las columnas que separamos del resto del dataset

descritores = list(set(list(data.columns))-set(target_column))
# creamos los descriptores o valores asociados a las categorias contenidas en los target_columns
# en esta linea se restan las columnas target del resto de columnas

X = data[descritores].values
y = data['target'].values
# asignamos valores de regresion a x e y 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=40)
# definimos el x e y de entrenamiento y de prueba
# test_size= divide el porsentaje 

regr_1 = DecisionTreeRegressor(max_depth=4)
# creamos el modelo de regresion (un modelo decisiontree)
regr_1.fit(X_train,y_train)
# .fit() ajusta el modelo a los parametros de entrenamiento
predict_train = regr_1.predict(X_train)
# .predict() nos da una prediccion basada en los parametros de entrenamiento o de prueba
predict_test = regr_1.predict(X_test)

print(classification_report(y_test,predict_test))
# imprimimos el reporte de clasificacion.

print(confusion_matrix(y_test,predict_test))
# arroja una matriz de diagonal, la diagonal debe tener valores y el resto deben ser ceros.
