from traceback import print_tb
import pandas as pd
from regex import P
from tqdm import tqdm
import warnings 

print("Cargando Exel ..... (.-.)")
Manzana =pd.read_excel("./Mas Cercano/Manzanas.xlsx",sheet_name="prueba id mznas",header=0)
df = pd.DataFrame()
df=df.assign(NOMBRE_COM='')
df=df.assign(CVE_VIALID='')
df=df.assign(Calle='')
df=df.assign(Numero='')

def SacarFaccionamientos (Manzana):
    FraccUnicos=[]
    for Fracc in tqdm(Manzana) :
        if Fracc not in FraccUnicos:
            FraccUnicos.append(Fracc)
    return FraccUnicos
def SacarIdManzanas (Manzana):
    Id=[]
    for idMa in tqdm(Manzana) :
        if idMa not in Id:
            Id.append(int(idMa))
    return Id
def SacarCalles (Manzana):
    Calle=[]
    for idMa in tqdm(Manzana) :
        if idMa not in Calle:
            Calle.append(idMa)
    return Calle
def ManzanaFracc (dicCalleNum,listaFracc):
    Aux=[]
    ct=0
    dicManzanaNUm={}
    for fracc in listaFracc:
        for manzana in Manzana['NOMBRE_COM']:
            if(str(manzana).count(fracc)==1):
                if Manzana.at[Manzana.index[ct],'CVE_VIALID'] not in Aux:
                    Aux.append(Manzana.at[Manzana.index[ct],'CVE_VIALID'])
            ct+=1
        dicManzanaNUm[fracc]=Aux
        Aux=[]
        ct=0
    return dicManzanaNUm
def QuitarLetras (cad):
    cad= str(cad).strip()
    cad= str(cad).replace(" ","-")
    cad= str(cad).replace("  "," ")
    posision=len(str(cad))
    for cadena in cad:
        if not (cadena.isdigit()):
            UltimaPosi=cad.index(cadena)
            NuevaCaden= str(cad)[0:UltimaPosi]
        else:
            NuevaCaden=str(cad)

    return str(NuevaCaden).replace(".0","")
def AgregarId (dicCalleNum,Manzana):
    Manzana=Manzana.assign(IdCalle='')
    c=0
    ct=0
    aux2=0
    aux=[]
    for celda in Manzana['NOMBRE_C_1']:
        if celda not in aux:
            aux.append(celda)
            ct+=1
        aux2=ct
        Manzana.at[Manzana.index[c],'IdCalle']=aux2
        aux2=0
        c+=1 
    Manzana.to_excel ("./Mas Cercano/Manzanas.xlsx",sheet_name="prueba id mznas", header=True,index=False)        
def AsignaridconId (manzana):
    IdMan=[]
    ct=0
    for celda in manzana['IdCalle']:
        IdMan.append([Manzana.at[Manzana.index[ct],'CVE_VIALID'],Manzana.at[Manzana.index[ct],'NOMBRE_C_1']])
        ct+=1
    return IdMan
def CompletarDatos(df,calle,minimo,maximo):
    Aux = []
    ListaCompletada=[]
    ct=0
    Aux = ListaCompletada
    for valor in range((maximo-minimo)+1):
        ListaCompletada.append(minimo+valor)
        ct+=1
    ct=0
    return ListaCompletada
listaFracc=(SacarFaccionamientos(Manzana['NOMBRE_COM']))
listaIdMan=(SacarIdManzanas(Manzana['CVE_VIALID']))
listaCalles=(SacarCalles(Manzana['NOMBRE_C_1']))
Aux=[]
ct=0
dicCalleNum={}
for calle in listaCalles:
    for CalleNum in Manzana['NOMBRE_C_1']:
        if(str(CalleNum).count(calle)==1):
            Aux.append((QuitarLetras(Manzana.at[Manzana.index[ct],'NUMERO_EXT'])))
        ct+=1
    dicCalleNum[calle]=Aux
    Aux=[]
    ct=0
dic2=ManzanaFracc(dicCalleNum,listaFracc)

AgregarId(dicCalleNum,Manzana)
'''print(AsignaridconId(Manzana))'''
cc=0

for celda in  tqdm(Manzana['NOMBRE_COM']):
    for idManzana in dic2[celda]:
        if (Manzana.at[Manzana.index[cc],'CVE_VIALID']==idManzana):
            for Numero in  dicCalleNum[Manzana.at[Manzana.index[cc],'NOMBRE_C_1']]:
                for numeroFinal in CompletarDatos(df,dicCalleNum[Manzana.at[Manzana.index[cc],'NOMBRE_C_1']],int(min(dicCalleNum[Manzana.at[Manzana.index[cc],'NOMBRE_C_1']])),int(max(dicCalleNum[Manzana.at[Manzana.index[cc],'NOMBRE_C_1']]))):
                        warnings.filterwarnings('ignore')
                        df = df.append({
                            'NOMBRE_COM':celda,
                            'CVE_VIALID':idManzana,
                            'Calle':Manzana.at[Manzana.index[cc],'NOMBRE_C_1'],
                            'Numero':numeroFinal
                        },
                        ignore_index=True
                        )
                        
    cc+=1    
df.to_excel ("./Mas Cercano/ElListo.xlsx", header=True,index=False)
