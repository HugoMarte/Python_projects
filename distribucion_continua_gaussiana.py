import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm 

def gaussian (x, mu, sigma):
  return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-0.5*pow((x-mu)/sigma,2))

#donde x es la variable alatoria, mu es la media de la distribucion y sigma es la STD

x = np.arange(-4,4,0.1)
y = gaussian (x, 0.0, 1.0)
plt.plot(x,y)

dist = norm(0, 1)
x = np.arange(-4,4,0.1)
y = [dist.pdf(value) for value in x]
plt.plot(x,y)

# calculando la distribución acumulada
dist = norm(0, 1)
x = np.arange(-4,4,0.1)
y = [dist.cdf(value) for value in x]
plt.plot(x, y)

df = pd.read_excel('s057.xls')
arr = df['Normally Distributed Housefly Wing Lengths'].values[4:]
values, dist = np.unique(arr, return_counts=True)
print(values)
plt.bar(values, dist)

# estimación de la distribución de probabilidad
mu = arr.mean()

#distribución teórica
sigma = arr.std()
dist = norm(mu, sigma)
x = np.arange(30,60,0.1)
y = [dist.pdf(value) for value in x]
# .pdf() densidad de probabilidad
plt.plot(x, y)

# datos
values, dist = np.unique(arr, return_counts=True)
plt.bar(values, dist/len(arr))