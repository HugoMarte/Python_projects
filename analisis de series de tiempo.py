from cProfile import label
import quandl 
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
#nos permite hacer descomposicion de series de tiempo tipo descomposicion de frecuencias Hz

QUANDL_API_KEY = '4sLKuvo8LszEsAF1Kqgr'  # Your Quandl key here
quandl.ApiConfig.api_key = QUANDL_API_KEY

data = quandl.get("FRED/GDP")
# quandl.get() trae un dataset 

df= quandl.get('CHRIS/CME_GC1', column_index=6, collapse='weakly', start_date='2010-01-01')
# column_index= llama a una sola columna
# collapse= determina los agrupamientos de las series de tiempo (hora,dia, semana, mes, año)
# start_date= establece el punto de inicio de nuestro df

df_settle=df['Settle'].resample('MS').ffill().dropna()
# "settle" es la columna de los valores que obtuve del proceso anterior.
# .reample() nos permite cambiar el agrupamiento de semanal a mensual ("MS")
# .ffill edita los datos que falten
# .dropna() 

df_rolling = df_settle.rolling(3)
# .rolling efectua operaciones agrupando por x numero de datos (cada 3 meses).

df_mean= df_rolling.mean()
de_std= df_rolling.std()

plt.figure(figsize=(12, 8))
plt.plot(df_settle, label="datos brutos")
plt.plot(df_mean, label= "media")
plt.legend()
plt.show()

decomp_res = seasonal_decompose(df.dropna(), freq=12)
# seasonal_decompose() nos da la frecuencia de la descomposicion 

df_trend= decomp_res.trend()
# .trend nos da la tendencia 
df_season= decomp_res.season()

de_residual= decomp_res.residual()