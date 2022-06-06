from lib2to3.pgen2.tokenize import tokenize
from turtle import numinput
import nltk
from numpy import indices
import pandas as pd
from tqdm import tqdm
df =pd.read_excel("./Catastro/Centroides.xlsx",sheet_name="Sheet2",header=0)
print("comparando Localidades")
df=df.assign(FactorDeCoincidencia='')
contcel=0
contadorCoincidencias=0
tokenizer =nltk.tokenize.TreebankWordTokenizer()
for indice in tqdm(range(int(len(df['CT_Localidad'])))):
    text=str(df.at[df.index[contcel],'CT_Localidad'])
    tokens=tokenizer.tokenize(text)
    
    text2=str(df.at[df.index[contcel],'NOM_LOCALI'])
    tokens2=tokenizer.tokenize(text2)
    for Index in tokens2:
        if((tokens.count(Index)!=0 and(tokens.count("LA")==0))):
            contadorCoincidencias+=1
    df.at[df.index[contcel],'FactorDeCoincidencia'] = contadorCoincidencias        
    if ((contadorCoincidencias!=0 )and((contadorCoincidencias/len(tokens2)<.5))):        
        df.at[df.index[contcel],'FactorDeCoincidencia'] = 0
    if ((contadorCoincidencias!=0 )and((contadorCoincidencias/len(tokens2)>=.5))):        
        df.at[df.index[contcel],'FactorDeCoincidencia'] = contadorCoincidencias
    
    contadorCoincidencias=0    
    contcel+=1
    pass
print("comparando Faccionamientos")
df=df.assign(FactorDeCoincidenciaCol='')
contcel=0
contadorCoincidencias=0
tokenizer =nltk.tokenize.TreebankWordTokenizer()
for indice in tqdm(range(int(len(df['CT_Fraccionamiento'])))):
    text=str(df.at[df.index[contcel],'CT_Fraccionamiento'])
    tokens=tokenizer.tokenize(text)
    
    text2=str(df.at[df.index[contcel],'NOMBRE_COM'])
    tokens2=tokenizer.tokenize(text2)
    for Index in tokens2:
        if(tokens.count(Index)!=0):
            
            contadorCoincidencias+=1 
    df.at[df.index[contcel],'FactorDeCoincidenciaCol'] = contadorCoincidencias        
    if ((contadorCoincidencias!=0 )and((contadorCoincidencias/len(tokens2)<.5))):        
        df.at[df.index[contcel],'FactorDeCoincidenciaCol'] = 0
    if ((contadorCoincidencias!=0 )and((contadorCoincidencias/len(tokens2)>=.5))):        
        df.at[df.index[contcel],'FactorDeCoincidenciaCol'] = contadorCoincidencias        
   
    contadorCoincidencias=0    
    

    contcel+=1
    pass
print("comparando Municipio")
df=df.assign(coMuni='')
contcel=0
contadorCoincidencias=0
tokenizer =nltk.tokenize.TreebankWordTokenizer()
for indice in tqdm(range(int(len(df['CT_Municipio'])))):
    text=str(df.at[df.index[contcel],'CT_Municipio'])
    tokens=tokenizer.tokenize(text)
    
    text2=str(df.at[df.index[contcel],'NOM_MUNICI'])
    tokens2=tokenizer.tokenize(text2)
    for Index in tokens2:
        if(tokens.count(Index)!=0):
            
            contadorCoincidencias+=1
    df.at[df.index[contcel],'coMuni'] = contadorCoincidencias         
    if ((contadorCoincidencias!=0 )and((contadorCoincidencias/len(tokens2)<.5))):        
        df.at[df.index[contcel],'coMuni'] = 0
    if ((contadorCoincidencias!=0 )and((contadorCoincidencias/len(tokens2)>=.5))):        
        df.at[df.index[contcel],'coMuni'] = contadorCoincidencias        
            
    
    contadorCoincidencias=0    
    

    contcel+=1
    pass
print("comparando Calle")
df=df.assign(CoCalle='')
contcel=0
contadorCoincidencias=0
tokenizer =nltk.tokenize.TreebankWordTokenizer()
for indice in tqdm(range(int(len(df['CT_Calle'])))):
    text=str(df.at[df.index[contcel],'CT_Calle'])
    tokens=tokenizer.tokenize(text)
    
    text2=str(df.at[df.index[contcel],'NOMBRE_C_1'])
    tokens2=tokenizer.tokenize(text2)
    for Index in tokens2:
        if(tokens.count(Index)!=0):
            contadorCoincidencias+=1
    df.at[df.index[contcel],'CoCalle'] = contadorCoincidencias        
    if ((contadorCoincidencias!=0 )and((contadorCoincidencias/len(tokens2)<.5))):        
        df.at[df.index[contcel],'CoCalle'] = 0
    if ((contadorCoincidencias!=0 )and((contadorCoincidencias/len(tokens2)>=.5))):        
        df.at[df.index[contcel],'CoCalle'] = contadorCoincidencias        


   
    contadorCoincidencias=0    
    

    contcel+=1
    pass
df.to_excel ("./Catastro/TodoFill2.xlsx", header=True,index=False)        
print("Fin")