import pandas as pd
import seaborn as sns
import altair as alt #libreria de graficos.
import plotly.express as px # libreria de graficos.

zoo_data= pd.read_csv(Zoo_data.csv)
zoo_name= ['animal name','hair','feathers','eggs','milk','airborne','aquatic','predator','toothed',
'backbone','breathes','venomous','fins','legs','tail','domestic',' cat-size','type']

zoo_data.info()
# .info nos da informacion sobre los conteos de frecuencias, los tipos de datos etc.

zoo_data.columns= zoo_name
# .columns= nos permite asignar nombres a las columnas.

alt.Chart(zoo_data).mark_line().encode(x='animal name',y='legs')
# .Chart nos permite definir el df a graficar.
# .mark_line() es el tipo de grafico (grafico de linea)
# .enocde() nos permite asignar valores a los ejes del grafico

alt.Chart(zoo_data).mark_bar().encode(x='animal name',y='legs')
# .mark_bar() en este caso el grafico sera de barras

fig = px.pie(zoo_data, values='aquatic', names='animal name', title='Porcentaje de animales acuáticos') # gráfica de pie 
fig.show() 
# .pie() es el tipo de grafico.
# El primer parametro es el df a graficar
# values= es la columna a graficar.
# names= es la columna de etiquetas.
# title= titulo del grafico.