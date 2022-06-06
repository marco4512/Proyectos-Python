import pandas as pd
from tqdm import tqdm
print("Cargando Exel ..... (.-.)")
Correctos =pd.read_excel("./Mas Cercano/mas cercano .xlsx",sheet_name="Hoja1",header=0)
NoCorrectos =pd.read_excel("./Mas Cercano/mas cercano .xlsx",sheet_name="Hoja2",header=0)
General =pd.read_excel("./Mas Cercano/mas cercano .xlsx",sheet_name="Hoja3",header=0)
IdFiltrados=[]
Correlones=[]
print("Cargando Datos Ya Encontrados  ..... (º-º)")
for Co in tqdm(Correctos['id de objeto']):
    Correlones.append(Co)
c=0
print("Filtrando Datos   ..... (¨-¨)")    
for Gene in tqdm(General['OBJECTID']):
    if Gene not in Correlones:
        IdFiltrados.append([General.at[General.index[c],'OBJECTID'],General.at[General.index[c],'NOMBRE_COM'],General.at[General.index[c],'NOMBRE_C_1'],General.at[General.index[c],'ext_1']])
    c+=1
DatosFiltrados =pd.DataFrame(IdFiltrados,columns=["OBJECTID","NOMBRE_COM","NOMBRE_C_1","ext_1"])
print("Guardando Datos   ..... (u-u)")   
DatosFiltrados.to_excel ("./Mas Cercano/Filtrado.xlsx", header=True,index=False)
print("Fin  ..... (7-7)")  