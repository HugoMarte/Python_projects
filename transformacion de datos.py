import pandas as pd
import plotly.express as px
import scipy.stats as ss 
# Libreria de estadistica

token_map_plot='pk.eyJ1IjoiY2hlbWlza3kiLCJhIjoiY2tnOGNhcXk3MGZ3eDJ5b2FxZ3ViajN1MyJ9.t3R24lWTwzTQwyJw4vuWFw'
# libreria de graficacion especifica para mapas.

df= pd.read_csv ("Accidentes en chicago.csv")

df["crash_data_2"] = df["Crash_Date"].apply(lambda x: pd.to_datetime(x, errors="coerce", UTC=True))
# .to_datetime() nos convierte el tipo de dato de la fecha de "onjeto" a "datetime"

df["unit_number_2"] = df["unit_num"].astype("int64")
# .astype nos cambia el tipo de dato. en este caso, de float a int64

px.set_mapbox_acess_token(token_map_plot)
px.scatter_mapbox(df, lat= "LATITUDE", lon= "LONGITUDE", color= "crash_hour", size= "unit_number_2",
color_continous_scale= px.colors.cyclical.icefire, size_max=15, zoom=10)
# _mapbox despliega nuestro grafico en un mapa, asociando latitud y longitud.

df["latitude_round"]= round(df ["LATITUDE"],2)
df["longitude_round"]= round(df ["LONGITUDE"],2)
# el modulo round nos permite redondear un numero a la cantidad de decimales especificados.

px.scatter_mapbox(df, lat= "latitude_round", lon= "longitude_round", color= "crash_hour", size= "unit_number_2",
color_continous_scale= px.colors.cyclical.icefire, size_max=15, zoom=10)
# con las latitudes y longitudes redondeadas, los puntos se convierten en una cuadricula.

pd.crosstab(index= df["POSTED_SPEED_LIMIT"], columns= "frecuencia")
# .crosstab genera una especie de tabla dinamica en pandas. 

