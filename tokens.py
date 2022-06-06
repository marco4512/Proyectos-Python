from lib2to3.pgen2.tokenize import tokenize
from turtle import numinput
import nltk
from numpy import indices
import pandas as pd
from tqdm import tqdm
tokenizer =nltk.tokenize.TreebankWordTokenizer()
GeneralFiltrado =pd.read_excel("./Mas Cercano/mas cercano .xlsx",sheet_name="Hoja1",header=0)
cont=0
cont2=0
cont3=0
for Caracter2 in tqdm(GeneralFiltrado['PP_numeroExterior']):
    cont3+=1
print(cont3)
for Caracter2 in tqdm(GeneralFiltrado['PP_numeroExterior']):
    for C in str(Caracter2):
        if (str(C).isalpha()or str(C).count("-")==1):
          GeneralFiltrado.at[GeneralFiltrado.index[cont2],'PP_numeroExterior']=str(GeneralFiltrado.at[GeneralFiltrado.index[cont2],'PP_numeroExterior']).replace(C," ")
        tokens=tokenizer.tokenize(str(GeneralFiltrado.at[GeneralFiltrado.index[cont2],'PP_numeroExterior']))
    if (len(tokens)!=0):
        GeneralFiltrado.at[GeneralFiltrado.index[cont2],'PP_numeroExterior']=tokens[0]
    cont2+=1
pass
GeneralFiltrado['PP_numeroExterior'].replace("-","")
GeneralFiltrado['PP_numeroExterior'].replace(".","")
GeneralFiltrado['PP_numeroExterior'].replace("|","")
GeneralFiltrado['PP_numeroExterior'].replace("/","")
GeneralFiltrado['PP_numeroExterior'].replace(" ","")
GeneralFiltrado['PP_numeroExterior'].replace("  ","")
GeneralFiltrado['PP_numeroExterior'].replace("   ","")
GeneralFiltrado['PP_numeroExterior'].fillna('0', inplace=True)
GeneralFiltrado.to_excel ("./Mas Cercano/SiEncontradosFiltrados.xlsx", header=True,index=False)

