import pandas as pd
df =pd.read_excel("./temp/FiltroUno.xlsx",sheet_name="Hoja1",header=0)
df2 =pd.read_excel("Filtro2.xlsx",sheet_name="Hoja1",header=0)
for indice in len(df['CT_Calle']):
    print(indice)
    