import numpy as np
from numpy.random import binomial
import matplotlib.pyplot as plt
from scipy.stats import binom
from math import factorial

def my_binomial(k,n,p):
  return factorial(n)/(factorial (k)*factorial(n-k))*pow(p,k)*pow(1-p,n-k)
#donde "k" es el numero de exitos, "n" es el numero de lanzamientos y "p" es la probabilidad de exito.
# Factorial() se explica solo
# pow(,) nos permite hacer potencias el primer numero es la base y despues de la coma el exponente

my_binomial(2,3,0.5)
# quiero saber, lanzando una moneda, la probabilidad de obtener dos caras, en tres lanzamientos,
# si la probabilidad de que salga cara es del 50%.

dist = binom (3, 0.5)
dist.pmf(2)
# binom() nos calcula la distribucion binomial con el numero de intentos y la probabilidad 
# esta funcion la importamos desde scipy.stats.
# .pmf() nos permite especificar el numero de aciertos que esperamos.
# pmf probability mass function

dist.cdf(2)
# .cdf calcula la probabilidad acumulada
# .cdf cumulative density function

p=0.5
n= 10
binomial(n,p)
# binomial() nos permite calcular la cantidad de aciertos segun la probabilidad y el numero 
# de ensayos
# con una probabilidad del 50% cuantos de los 10 lanzamientos seran cara

exp=[]
for i in range (100):
  exp.append(binomial(n,p))
#creamos una lista de 100 trials que recogera los resultados de lanzar la moneda 10 veces en 100 trials.

np.unique(exp, return_counts=True)[1]/len(exp)
# .unique() identifica todos los elementos unicos de una lista.
# return_counts= nos devuelve la cantidad de veces que aparecen los elementos unicos.
# [1] reresenta la segunda lista, la de la cantidad de veces que aparece cada elemento.
# len() nos dice la lingitud del arreglo.
# dividiendo [1]/longitud del arreglo, nos da la probabilidad de cada elemento independiente.

n=3
p=0.5
def plot_exp (num_trials):
  values = [0,1,2,3]
  arr=[]
  for i in range (num_trials):
    arr.append(binomial(n,p))
  sim = np.unique(arr, return_counts=True)[1]/len(arr)
  teorica = [binom(3,0.5).pmf(k) for k in values]
  plt.bar(values, sim, color = "red")
  plt.bar(values, teorica, alpha = 0.5, color = "blue")
  plt.title ("{} numero de esperimentos".format(num_trials))
  plt.show()

