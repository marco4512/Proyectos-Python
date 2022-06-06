#28-04-22 11:28
import openpyxl
from cupshelpers import Printer
import pandas as pd
from regex import P
from tqdm import tqdm
import warnings
import numpy as np

print("Cargando Exel ..... (.-.)")
Manzana =pd.read_excel("./Mas Cercano/mnzOp.xlsx",sheet_name="Sheet2",header=0,engine = 'openpyxl')
NoEncontrados=pd.read_excel("./Mas Cercano/LosChidos.xlsx",sheet_name="Sheet2",header=0,engine = 'openpyxl')
CeldaMuni='NOM_MUNICI'
CeldaColonia='NOMBRE_COM'
CeldaCalle='NOMBRE_C_1'
CeldaLocali='NOM_LOCALI'
CeldaManzana='id mzna'
CeldaNumero='NUMERO_EXT'

def Solo_No_Encontrados ():
    NoEncontrados=pd.read_excel("./Mas Cercano/LosChidos.xlsx",sheet_name="Sheet2",header=0,engine = 'openpyxl')
    NoEncontrados['OBJECTID'].fillna('No Cercano',inplace=True)
    aux=[]
    for i,cel in enumerate(NoEncontrados['OBJECTID']):
        if(str(cel).count("No Cercano")):
            aux.append([NoEncontrados.at[NoEncontrados.index[i],'frac catastro'],NoEncontrados.at[NoEncontrados.index[i],'calle catastro'],NoEncontrados.at[NoEncontrados.index[i],'PP_numeroExterior'],cel])
    return(aux)
    
def Completar  (min,calle,muni,mzn,localidad,col):
    Digitos= len(str(min))
    esParesImpar=ParInpar(int(float(min)))
    arreglofin=[]
    if(Digitos==1):
       
        for cant in range(1,10):
            if(esParesImpar):
                if(cant % 2 == 0 ):
                    arreglofin.append([muni,localidad,mzn,col,calle,cant])
            else:
                if not(cant % 2 == 0 ):
                    arreglofin.append([muni,localidad,mzn,col,calle,cant])

    if(Digitos==2):
       
        iniciador=str(min)[0]+'0'
        for cant in range(int(iniciador),100):
            if(esParesImpar):
                if(cant % 2 == 0 ):
                    arreglofin.append([muni,localidad,mzn,col,calle,cant])
            else:
                if not(cant % 2 == 0 ):
                   arreglofin.append([muni,localidad,mzn,col,calle,cant])
    if(Digitos==3):
   
        iniciador=str(min)[0]+'00'
        for cant in range(int(iniciador),1000):
            if(esParesImpar):
                if(cant % 2 == 0 ):
                    arreglofin.append([muni,localidad,mzn,col,calle,cant])
            else:
                if not(cant % 2 == 0 ):
                    arreglofin.append([muni,localidad,mzn,col,calle,cant])

    if(Digitos==4):
        
        iniciador=str(min)[0]+'000'
        for cant in range(int(iniciador),10000):
            if(esParesImpar):
                if(cant % 2 == 0 ):
                   arreglofin.append([muni,localidad,mzn,col,calle,cant])
            else:
                if not(cant % 2 == 0 ):
                    arreglofin.append([muni,localidad,mzn,col,calle,cant])

    if(Digitos==5):
        
        iniciador=str(min)[0]+'0000'
        for cant in range(int(iniciador),100000):
            if(esParesImpar):
                if(cant % 2 == 0 ):
                    arreglofin.append([muni,localidad,mzn,col,calle,cant])
            else:
                if not(cant % 2 == 0 ):
                    arreglofin.append([muni,localidad,mzn,col,calle,cant])
    return(arreglofin)

def ParInpar (Numero):
    if( Numero % 2 == 0 ):
        return True
    else:
        return False
def QuitarLetras (cadena):
    ct=0
    cadfin=0
    cf=''
    for ca in cadena:
        if (str(ca).isalpha()or(str(ca).count(" "))or(str(ca).count("/"))or(str(ca).count("-"))):
            cadfin=(ct)
        ct+=1
    if cadfin==0:
        cf=cadena
    else:
        cf=cadena[0:cadfin]

    cf= str(cf).strip()
  
    return(cf)
def SacarUnicos(NombreDeLaCelda):
    Aux=[]
    for Muni in Manzana[NombreDeLaCelda]:
        if Muni not in Aux:
            Aux.append(Muni)
    return(Aux)
def procesandocalles (calle,mnz):
    axu=[]
    for c,celda in enumerate(Manzana[CeldaCalle]):
        if(str(calle).count(celda)==1 and mnz==Manzana.at[Manzana.index[c],CeldaManzana]):
            axu.append(QuitarLetras(QuitarLetras(str(Manzana.at[Manzana.index[c],CeldaNumero]))))

    return axu






#Aqui se declaran los arreglos con los valores no repetidos de cada uno de los campos
Municipio=SacarUnicos(CeldaMuni)
Localidad=SacarUnicos(CeldaLocali)
Mz=SacarUnicos(CeldaManzana)
Colonia=SacarUnicos(CeldaColonia)
Calle=SacarUnicos(CeldaCalle)
c=0
aux=[]
numeroAux=[]
arreglofin=[]
df2 = pd.DataFrame()
df2['NOM_MUNICI'] = ""
df2['NOM_LOCALI'] = ""
df2['id mzna'] = ""
df2['NOMBRE_COM'] = ""
df2['NOMBRE_C_1'] = ""
df2['NUMERO_EXT'] = ""
valores_No_Encontrados=[]
print("Procesando los no encontrados <.-.>")
for valor in Solo_No_Encontrados():
    if valor not in valores_No_Encontrados:
        valores_No_Encontrados.append([valor[0],valor[1],valor[2]])
idx = 0
megaa=[]
ok=[]
def guardar (arreglo,idx):
    for i,e in enumerate(arreglo):
                for i2, e2 in enumerate(arreglo[i]):
                    #megaa.append(e2)
                    aux=[e2[3],e2[4],e2[5]]
                    ok.append(aux)
                    '''if aux in valores_No_Encontrados:
                        megaa.append(e2)'''
                    #Solo_Iguales(e2,valores_No_Encontrados)
                    idx += 1

def Solo_Iguales (e2,valores_No_Encontrados):
    for celda_Dos in valores_No_Encontrados:
        if(str(e2[3]).count(celda_Dos[0])and(str(e2[4]).count(celda_Dos[1]))and(e2[5]==celda_Dos[2])):
            print(e2)

            



def manza (loca,aux,muni):
    for mnz in tqdm (Mz):
            #Recorremos la manzana
            for col in Colonia:
                for c,celda in enumerate(Manzana[CeldaManzana]):
                    if (mnz==celda):
                        if Manzana.at[Manzana.index[c],CeldaCalle] not in aux:
                            aux.append(Manzana.at[Manzana.index[c],CeldaCalle])
                for ca in aux:
                    if Completar(min(procesandocalles(ca,mnz)),ca,muni,mnz,loca,col) not in arreglofin:
                        
                        arreglofin.append(Completar(min(procesandocalles(ca,mnz)),ca,muni,mnz,loca,col))
                guardar(arreglofin,idx)        
                aux=[]
                numeroAux=[]
                c=0

def localin (muni,aux):
     for loca in Localidad:
        #Aqui se recorre la localidad por municipio
        manza(loca,aux,muni)
        

for muni in  tqdm (Municipio):
    #Aqui se recorre el municipio
    localin(muni,aux)
auxx=[]
auxmegga=[]
au=[]
bande=0
bande2=0
'''for celda_uno in tqdm(megaa):
    for celda_Dos in valores_No_Encontrados:
        #Solo_Iguales (au,celda_uno,celda_uno[3],celda_uno[4],celda_uno[5],celda_Dos[0],celda_Dos[1],celda_Dos[2])
        if(bande==0):
            if((str(celda_uno[3]).count(celda_Dos[0]))):
                bande2=1
                
                au.append(celda_uno)
            else:
                if(bande2==1):
                    
                    bande==1
        else:
            break'''
'''
for i,celda in enumerate(tqdm(megaa)):
    for i,celda_No_Encontrada in enumerate((NoEncontrados)):
        print()
'''
'''
if(len(auxmegga)>1000000):
    Bloques= int(round(len(megaa)/1000000))
    print(Bloques)
    auxcn=1000000
    axucw=1
    aux=[]
    for chunk in tqdm(range(Bloques)):
        if auxcn<(len(megaa)):
            print()
        else:
            auxcn=int(len(megaa))-1
        print((len(megaa)))
        print(axucw,auxcn,"   ",(auxcn-axucw))
        df2 = pd.DataFrame(megaa[axucw:auxcn])
        aux.append(df2.iloc[axucw:auxcn])
        aux[chunk].to_csv('./Mas Cercano/OUT/SeraEsteElFin '+str(chunk)+'.csv') 
        axucw=auxcn
        auxcn+=1000000
df2 = pd.DataFrame(auxmegga)'''
print(len(ok))
indice=[]
for valor in tqdm(valores_No_Encontrados):
    try:
        indice.append(ok.index(valor))
    except:
        continue
for valorXD in tqdm(indice):
    print(ok[valorXD])

#print(megaa.index(['AGUASCALIENTES', 'AGUASCALIENTES', 10616, 'BARRIO LA PURISIMA', 'CALLE EZEQUIEL A CHAVEZ', 222]))
'''df2 = pd.DataFrame(indice)
df2.to_excel ("./Mas Cercano/SoloEncontrados3.xlsx", header=True,index=False)
'''


