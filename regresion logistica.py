from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd
import seaborn as sns

def likelihood(y,yp):
  return yp*y+(1-yp)*(1-y) #ecuacion de verosimilitud.

fig = plt.figure()
axe= fig.gca(projection="3d")
#.gca(projection="3d") genera un grafico de tres dimensiones

Y= np.arange(0,1,0.01)
YP = np.arange(0,1,0.01)
Y, YP= np.meshgrid (Y,YP)
Z= likelihood(Y, YP)
surf = axe.plot_surface(Y, YP, Z, cmap= cm.coolwarm)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

#-----------------------------------------------------------------------------------------------
# Regresion logistica con scikit learn

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

atrib_names = ['sepal length', 'sepal width', 'petal length', 'petal width']
X, y = load_iris(return_X_y=True)

clf = LogisticRegression(random_state=10, solver= "liblinear").fit(X[:100], y[:100])
# LogisticRegresion es una funcion de sklearn que genera regresiones logisticas
# random_state= es un generador aleatorio que inicializa las variables del modelo 
# solver= es el metodo de optimizacion del modelo (encuentra la mejor combinacion de los parametros)

clf.coef_
# .coef_ nos muesta la matriz de coeficientes (betas) que mejor ajustan los parametros del modelo
# de clasificacion (YP), a las categorias dadas por los datos reales (Y).

