import pandas as pd
chicago_data='https://raw.githubusercontent.com/terranigmark/curso-analisis-exploratorio-datos-platzi/main/Traffic_Crashes1.csv'

df= pd.read_csv(chicago_data)

df["CRASH_DATE"]= df["CRASH_DATE"].apply(lambda x: pd.to_datetime(x,errors="coerce", utc=True))
# convertimos los datos de la columna "crash_date" a unidad de tiempo

df.groupby(['LIGHTING_CONDITION','REPORT_TYPE','CRASH_HOUR']).agg({'BEAT_OF_OCCURRENCE':'sum',})
# .groupby nos permite agrupar columnas

pd.pivot_table(df, index=["LIGHTING_CONDITION","REPORT_TYPE"])
# .pivot_table nos crea una tabla dinamica 
# index=[] nos permite especificar las columnas de la tabla.

df.filter(["REPORT_TYPE","CRASH_DAY_OF_WEEK"],axis=1)
# .filter nos permite filtrar por columnas 

cross_table=pd.crosstab(df["REPORT_TYPE"], df["REPORT_TYPE"])
# .crosstab genera una tabla cruzada.

