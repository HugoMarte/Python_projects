import pandas as pd
import seaborn as sns
import altair as alt #libreria de graficos.
import plotly.express as px # libreria de graficos.

df= pd.read_csv(Chicago_crashes.csv)

report1= df.groupby(["LIGHTING_CONDITION", "REPORT_TYPE", "CRASH_HOUR"]).agg({"NUM_UNITS":"sum"})
#.groupby() nos permite crear una pequeña matrix agregada de dstos del dataframe original.
# .agg({}) crea columnas agregadas en las que podemos hacer operaciones con sus valores
report1= report1.reset_index()
# .reset_index() elimina la columna de indices duplicada en el proceso de .groupby

report1= df.groupby(["LIGHTING_CONDITION", "REPORT_TYPE", "CRASH_HOUR"]).agg({"POSTED_SPEED_LIMIT":[
    "sum", "min", "max", ]})
# En este caso la columna .agg({}) se va a dividir en tres sub columnas cada una con una operacion.