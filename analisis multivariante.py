import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

url='https://raw.githubusercontent.com/terranigmark/curso-analisis-exploratorio-datos-platzi/main/train_titanic.csv'

df_titanic= pd.read_csv(url, error_bad_lines= False)

df_titanic.shape
# .shape nos dice cuantas filas y columnas tiene un df

nulls= df_titanic.isnull().sum().sort_values(ascending=False)
# .isnull() nos dice cuantos campos vacios o nulos tenemos en una columna
# .sum() suma los valores.
# .sort_values() ordena los valores de menor a mayor.
# ascending= False invierte el orden de menor a mayor.

women= df_titanic.loc[df_titanic.Sex == "female"]["survived"]
mean_women= sum(women)/ len(women) # aqui se calcula el promedio de mujeres que sobrevivieron.

men= df_titanic.loc[df_titanic.Sex == "male"]["survived"]
mean_men= sum(men)/ len(men)

df_titanic ["survived"]= df_titanic ["survived"].map({0:"not_survived", 1:"survived"})
# .map({}) nos permite convertir una variable numerica a categorica.

sns.distplot(df_titanic["Age"].dropna())
# .dropna() deja fuera los valores NaN de una columna.

df_titanic["Embarked"]= df_titanic["Embarked"].map({"S":0, "C":2, "Q":2,"Nan":0})

p_corr_embarked = df_titanic.corr(method="pearson")
# en .cor() 
# method= nos permitre agregar el metodo de calculo de correlacion.

