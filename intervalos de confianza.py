import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as st

np.random.seed(20)
x= np.random.randint(0,10,10)
y= x+ np.random.normal(0,1,10)

grafico= sns.regplot(x,y, ci=80)
#grafico de regresion con seaborn

tuple = list(zip(x,y))
# Unimos las variables var1 y var2 (estamos creando un tuple) a partir de zip

df= pd.DataFrame(tuple, columns = ["vacaciones", "gasto"])
# Transformamos el tuple a un data frame a partir de DataFrame

st.t.interval(alpha=0.95, df = len(df)-1, loc= np.mean(df),scale=st.sem(df))
# Calcula los intervalos de confianza a un 95% para ambas variables