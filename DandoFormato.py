from lib2to3.pgen2.tokenize import tokenize
from turtle import numinput
import nltk
from numpy import indices
import pandas as pd
from tqdm import tqdm
df =pd.read_excel("./temp/FiltroDos.xlsx",sheet_name="Sheet1",header=0)
df['CT_Calle'] = df['CT_Calle'].str.replace('SN', '')
df['CT_Calle'] = df['CT_Calle'].str.replace('S/N', '')
df['CT_Calle'] = df['CT_Calle'].str.replace('#', '')
df['CT_Calle'] = df['CT_Calle'].str.replace('º', '')
df['CT_Calle'] = df['CT_Calle'].str.replace('.', '')
contcel=0
contToken=0
numInterior=''
numExterior=''
Domicilio=''
tokensss=0
numIn=''
intexx=''
tokenizer =nltk.tokenize.TreebankWordTokenizer()
for indice in tqdm(range(int(len(df['CT_Calle'])))):
    text=str(df.at[df.index[contcel],'CT_Calle'])
    tokens=tokenizer.tokenize(text)
    inte=str(df.at[df.index[contcel],'PP_numeroExterior'])
    intexx=inte
    intexx=intexx.replace('.0', '')
    inte2=str(df.at[df.index[contcel],'PP_Interior'])
 
    for indice2 in tokens:
        
        if(indice2==intexx):

            df.at[df.index[contcel],'CT_Calle'] = str(df.at[df.index[contcel],'CT_Calle']).replace(indice2, '')
        
      
    contcel+=1
    pass
df['CT_Calle'] = df['CT_Calle'].str.strip()
df.to_excel ("./temp/Final.xlsx", header=True,index=False)