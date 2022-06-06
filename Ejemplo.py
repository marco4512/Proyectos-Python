from traceback import print_tb
import pandas as pd
from regex import P
from tqdm import tqdm
print("Cargando Exel ..... (.-.)")
Manzana =pd.read_excel("./Mas Cercano/Manzanas.xlsx",sheet_name="prueba id mznas",header=0)
df = pd.DataFrame()
df=df.assign(Calle='')
df=df.assign(Numero='')
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
def Calless(df,calle,minimo,maximo):
    Calle=[]
    ct=0
    for valor in range((maximo-minimo)+1):
        Calle.append(calle)
        ct+=1
    ct=0
    return Calle
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
print(ManzanaFracc(dicCalleNum,listaFracc))
axCalle=[]
axNUmero=[]
for num in dicCalleNum:
    print("Calle: ",num )
    print ((min(dicCalleNum[num])),(max(dicCalleNum[num])))
    print(Calless(df,num,int(min(dicCalleNum[num])),int(max(dicCalleNum[num]))))
    df['Calle']=Calless(df,num,int(min(dicCalleNum[num])),int(max(dicCalleNum[num])))
    df['Numero']=CompletarDatos(df,num,int(min(dicCalleNum[num])),int(max(dicCalleNum[num])))

df.to_excel ("./Mas Cercano/Comletado.xlsx", header=True,index=False)

