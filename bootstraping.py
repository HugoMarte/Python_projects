from gettext import npgettext
import pandas as pd
import numpy as np
import random

data= np.random.normal(loc=34, size= 10000)
# loc= es la media 
# size= es la cantidad de eventos 

promedio = []

for i in range (40):
  muestra = random.sample (data.tolist(), 5)
  prom= np.mean(muestra)
  promedio.append(prom)