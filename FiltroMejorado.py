from lib2to3.pgen2.tokenize import tokenize
from turtle import numinput
import nltk
import pandas as pd
from tqdm import tqdm
print("Se lee el archivo")
df =pd.read_excel("sedrae.xlsx",sheet_name="Hoja1",header=0)
df['CT_Calle'] = df['CT_Calle'].str.upper()
df['CT_Fraccionamiento'] = df['CT_Fraccionamiento'].str.upper()
df['CT_Localidad'] = df['CT_Localidad'].str.upper()
df['CT_Municipio'] = df['CT_Municipio'].str.upper()
'''Se elimian espacios atras y adelante'''
df['CT_Calle'] = df['CT_Calle'].str.strip()
df['CT_Fraccionamiento'] = df['CT_Fraccionamiento'].str.strip()
df['CT_Localidad'] = df['CT_Localidad'].str.strip()
df['CT_Municipio'] = df['CT_Municipio'].str.strip()

df=df.assign(CT_Estado='AGUASCALIENTES')
df = df.reindex(columns=['CT_Estado','CT_Municipio','CT_Localidad','CT_Fraccionamiento','CT_Calle'])
   
df['CT_Municipio'] = df['CT_Municipio'].str.replace('Í', 'I')
df['CT_Municipio'] = df['CT_Municipio'].str.replace('Á', 'A')
df['CT_Municipio'] = df['CT_Municipio'].str.replace('É', 'E')
df['CT_Municipio'] = df['CT_Municipio'].str.replace('Ó', 'O')
df['CT_Municipio'] = df['CT_Municipio'].str.replace('Ú', 'U')

df['CT_Localidad'] = df['CT_Localidad'].str.replace('Í', 'I')
df['CT_Localidad'] = df['CT_Localidad'].str.replace('Á', 'A')
df['CT_Localidad'] = df['CT_Localidad'].str.replace('É', 'E')
df['CT_Localidad'] = df['CT_Localidad'].str.replace('Ó', 'O')
df['CT_Localidad'] = df['CT_Localidad'].str.replace('Ú', 'U')

df['CT_Fraccionamiento'] = df['CT_Fraccionamiento'].str.replace('Í', 'I')
df['CT_Fraccionamiento'] = df['CT_Fraccionamiento'].str.replace('Á', 'A')
df['CT_Fraccionamiento'] = df['CT_Fraccionamiento'].str.replace('É', 'E')
df['CT_Fraccionamiento'] = df['CT_Fraccionamiento'].str.replace('Ó', 'O')
df['CT_Fraccionamiento'] = df['CT_Fraccionamiento'].str.replace('Ú', 'U')

df['CT_Calle'] = df['CT_Calle'].str.replace('Í', 'I')
df['CT_Calle'] = df['CT_Calle'].str.replace('Á', 'A')
df['CT_Calle'] = df['CT_Calle'].str.replace('É', 'E')
df['CT_Calle'] = df['CT_Calle'].str.replace('Ó', 'O')
df['CT_Calle'] = df['CT_Calle'].str.replace('Ú', 'U')
df['CT_Calle'] = df['CT_Calle'].str.replace('-', ' ')
df['CT_Calle'] = df['CT_Calle'].str.replace('NA', '')
df['CT_Calle'] = df['CT_Calle'].str.replace('SN', 'S/N')
df['CT_Calle'] = df['CT_Calle'].str.replace('  ', ' ')
df['CT_Calle'].fillna('null', inplace=True)
df=df.assign(PP_numeroExterior='null')
df=df.assign(PP_Interior='null')
contcel=0
contToken=0
numInterior=''
numExterior=''
Domicilio=''
tokenizer =nltk.tokenize.TreebankWordTokenizer()
for indice in tqdm(range(int(len(df['CT_Calle'])))):
    text=df.at[df.index[contcel],'CT_Calle']
    tokens=tokenizer.tokenize(text)
    
    for indice2 in tokens:
        if(len(indice2)<3 and indice2.isnumeric()):
            numInterior=indice2
            
        if((len(indice2)<5) and(len(indice2)>=3) and (indice2.isnumeric())):
            numExterior=indice2
            
        if(len(indice2)<3 and indice2.isalnum()and(indice2!='DE')and(indice2!='LA')and(indice2!='EL')and(indice2!='AV')and(indice2!='CP')and(indice2!='KM')and(indice2!='MA')and(indice2!='MI')and(indice2!='DC')and(indice2!='II')and(indice2!='ED')):
            numInterior=indice2
           
        if((len(indice2))<3 and (indice2.isalnum())and(numExterior=='')and(len(numExterior)!=1)):
            numExterior=numInterior
            numInterior='null'
        
            
        contToken+=1

    df.at[df.index[contcel],'PP_Interior']=numInterior
    df.at[df.index[contcel],'PP_numeroExterior']=numExterior
  
    numInterior=''
    numExterior=''
    Domicilio=''     
    contcel+=1
    pass
  
df.to_excel ("./temp/FiltroUno.xlsx", header=True,index=False)
print("***********Fin***********")