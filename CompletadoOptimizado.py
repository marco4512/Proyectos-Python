#28-04-22 11:28
from cupshelpers import Printer
import pandas as pd
from regex import P
from tqdm import tqdm
import warnings 
print("Cargando Exel ..... (.-.)")
Manzana =pd.read_excel("./Mas Cercano/mnzOp.xlsx",sheet_name="Sheet2",header=0)
CeldaMuni='NOM_MUNICI'
CeldaColonia='NOMBRE_COM'
CeldaCalle='NOMBRE_C_1'
CeldaLocali='NOM_LOCALI'
CeldaManzana='id mzna'
CeldaNumero='NUMERO_EXT'
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
        if(str(calle).count(str(celda))==1 and mnz==Manzana.at[Manzana.index[c],CeldaManzana]):
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


idx = 0
megaa=[]
def guardar (arreglo,idx):
    for i,e in enumerate(arreglo):
                for i2, e2 in enumerate(arreglo[i]):
                    megaa.append(e2)
                    idx += 1
contcc=0
def manza (loca,aux,muni,contcc):
    Tamaño=(len(Manzana[CeldaManzana]))
    for mnz in tqdm(Mz):
            #Recorremos la manzana
            for col in Colonia:
                for c,celda in enumerate(Manzana[CeldaManzana]):
                   if(Tamaño>contcc):
                    if(mnz==Manzana.at[Manzana.index[contcc],CeldaManzana]):
                        aux.append(Manzana.at[Manzana.index[contcc],CeldaCalle])                        
                        contcc+=1
                    else:
                        break
                for ca in aux:
                    
                    if Completar(min(procesandocalles(str(ca),mnz)),ca,muni,mnz,loca,col) not in arreglofin:
                        arreglofin.append(Completar(min(procesandocalles(ca,mnz)),ca,muni,mnz,loca,col))
                guardar(arreglofin,idx)        
                aux=[]
                numeroAux=[]
                c=0

def localin (muni,aux):
     for loca in Localidad:
        #Aqui se recorre la localidad por municipio
        manza(loca,aux,muni,contcc)
        

for muni in  tqdm (Municipio):
    #Aqui se recorre el municipio
    localin(muni,aux)
auxx=[]

df2 = pd.DataFrame(megaa)
df2.to_csv('./Mas Cercano/forzado2.csv', sep=',')