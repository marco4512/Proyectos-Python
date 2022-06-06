from sqlite3 import Row
import pandas as pd
from tqdm import tqdm
print("Se lee el archivo")
df =pd.read_excel("./temp/Sedec2.xlsx",sheet_name="Sheet1",header=0)
contcel=0
contvac=0
caracter=''
contCarmenos=0
cont=0
cont2=0

df['PP_numeroExterior'].fillna('null', inplace=True)
df['CT_Calle'].fillna('null', inplace=True)
df['CT_Calle'] = df['CT_Calle'].str.strip()
for indice in tqdm(range(int(len(df['CT_Calle'])))):
    contCarmenos=df.at[df.index[contcel],'CT_Calle']
    contCarmenos=len(str(contCarmenos))
    num=''
    PosPrimerEspacio=0
    direccion=''
    if(df.at[df.index[contcel],'PP_numeroExterior']=='null'):
        for indice2 in range(len(df.at[df.index[contcel],'CT_Calle'])):
            caracter = df.at[df.index[contcel],'CT_Calle']
            cont+=1
            contCarmenos-=1
        cont2=(cont-1)
        cont3=cont2+1
        for indice3 in range(len(df.at[df.index[contcel],'CT_Calle'])):
            cont3-=1
            
            while((caracter[cont2].isdigit())and(caracter[cont3]!=' ')):
                
                num=num+caracter[cont2]
                cont2-=1
        cont=0
    PosPrimerEspacio=len(num)
    
    num=num[::-1]
    Ultimo=len((str(df.at[df.index[contcel],'CT_Calle'])))
    Ultimo=Ultimo-PosPrimerEspacio
    direccionAux=str(df.at[df.index[contcel],'CT_Calle'])
    direccion=direccionAux[0:Ultimo]    
    '''print("Num: ",num)
    print("Calle: ",direccion)'''
    if(df.at[df.index[contcel],'PP_numeroExterior']=='null'):
        df.at[df.index[contcel],'CT_Calle']=str(direccion)
        df.at[df.index[contcel],'PP_numeroExterior']=str(num)
    contcel+=1
    pass
nombreArchivo ='Filtro2' 
nombreArchivo=nombreArchivo+".xlsx"   
df.to_excel (nombreArchivo, header=True,index=False)
