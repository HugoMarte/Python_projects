from locale import normalize
import numpy as np
from numpy.random import normal
from scipy.stats import norm
import matplotlib.pyplot as plt

sample = normal(size= 1000)
# normal(size=) nos genera un conjunto aleatorio de numeros de "size=" cantidad.

plt.hist(sample, bins=30)
plt.show()
# graficamos "sample"

sample2= normal(loc=50, scale=5, size=100)
# loc= corresponde al promedio
# scale= corresonde a SDT

mu = sample2.mean()
# mu sera la media del arreglo "sample2"
sigma = sample2.std()
# sigma sera la std del arreglo "sample2"

# CALCULO DE DISTRIBUCION NO PARAMETRICO

from numpy import hstack
from sklearn.neighbors import KernelDensity

#construimos una distribución bimodal
sample1 = normal(loc=20, scale=5, size=300)
sample2 = normal(loc=40, scale=5, size=700)
sample = hstack((sample1, sample2))
# hstack(()) nos permite agrupar dos distribuciones para crear una curva con dos campanas

model = KernelDensity(bandwidth=2, kernel='gaussian')
sample = sample.reshape((len(sample), 1))
model.fit(sample)

values = np.asarray([value for value in range(1, 60)])
values = values.reshape((len(values), 1))
probabilities = model.score_samples(values) #probabilidad logarítmica
probabilities = np.exp(probabilities)  # inversión de probabilidad

plt.hist(sample, bins=50, density=True) 
plt.plot(values[:], probabilities)
plt.show()