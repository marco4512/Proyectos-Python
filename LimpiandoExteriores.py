from lib2to3.pgen2.tokenize import tokenize
from turtle import numinput
import nltk
import pandas as pd
from tqdm import tqdm
print("Se lee el archivo")
df =pd.read_excel("./temp/FiltroUno.xlsx",sheet_name="Sheet1",header=0)
df['PP_numeroExterior'].fillna('null', inplace=True)

contcel=0
contToken=0
numInterior=''
numExterior=''
Domicilio=''
tokensss=0
numIn=''
tokenizer =nltk.tokenize.TreebankWordTokenizer()
for indice in tqdm(range(int(len(df['PP_numeroExterior'])))):
    text=str(df.at[df.index[contcel],'PP_numeroExterior'])
    tokens=tokenizer.tokenize(text)
    numIn=str(df.at[df.index[contcel],'PP_Interior'])
    for indice2 in tokens: 
        if(indice2.isalpha()and(numIn.isnumeric())):
            numExterior=numExterior+""+numIn
        if(indice2.isalpha()and(indice2!="null")and(len(indice2)==1)):
            df.at[df.index[contcel],'PP_numeroExterior']="null"
        if(indice2.isalnum()and(indice2!="null")and(len(indice2)==2)and(not indice2.isnumeric())):
            print(indice2)
            df.at[df.index[contcel],'PP_numeroExterior']="null"
            df.at[df.index[contcel],'PP_Interior']=indice2
       
             
        contToken+=1
    
    if(numExterior!=""):
      
       df.at[df.index[contcel],'PP_numeroExterior']=numExterior
    
    if(numExterior==numIn):
       df.at[df.index[contcel],'PP_Interior']="null" 
    
    numInterior=''
    numExterior=''
    Domicilio=''
    contcel+=1
    
    
    pass

df.to_excel ("./temp/FiltroDos.xlsx", header=True,index=False)

print("***********Fin***********")