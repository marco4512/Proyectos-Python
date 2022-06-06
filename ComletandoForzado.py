from fcntl import DN_DELETE
import pandas as pd
from regex import P
from tqdm import tqdm
import warnings 
print("Cargando Exel ..... (.-.)")
Manzana =pd.read_excel("./Mas Cercano/Manzanas (1).xlsx",sheet_name="prueba id mznas",header=0)
ColIdManzana='CVE_VIALID'
ColCalle='NOMBRE_C_1'
ColNumExt='NUMERO_EXT'
ColColonia='NOMBRE_COM'
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
def SacandoCallesUnicas ():
    aux=[]
    for calle in Manzana[ColCalle]:
        if calle not in aux:
            aux.append(calle)
    return aux
def ManzanasUnicas ():
    aux=[]
    for idManzana in Manzana[ColIdManzana]:
        if idManzana not in aux:
            aux.append(idManzana)
    return aux
SacandoCallesUnicas()
calles= SacandoCallesUnicas()
id= ManzanasUnicas()
def CompletarNumero (min,max,auxiliarcalle,auxiliarManzana,auxiliarColonia):
    Valores=[]
    for valor in range(((int(max))-(int(min))+1)):
        if [auxiliarColonia,auxiliarManzana,auxiliarcalle,(min+valor)] not in Valores:
            Valores.append([auxiliarColonia,auxiliarManzana,auxiliarcalle,(min+valor)])
    return Valores
megaaux=[]
def megaArreglo (arreglo,megaaux):
    for celda in arreglo:
        megaaux.append(celda)

def SacarRangosPorCalle (calles,ID):
    cont=0
    numeros=[]
    ArregloFIn=[]
    auxiliarcalle=''
    auxiliarManzana=''
    auxiliarColonia=''
    print(ID)
    for id in  tqdm(ID):
        for calle in calles:
            for celda in Manzana[ColCalle]:
                if(id == Manzana.at[Manzana.index[cont],ColIdManzana]):
                    #print("entro2",calle, " - ",celda )
                    if ((str(calle).count(str(celda))==1)):
                        QuitarLetras(Manzana.at[Manzana.index[cont],ColNumExt])
                        numeros.append(int(QuitarLetras(Manzana.at[Manzana.index[cont],ColNumExt])))
                        auxiliarcalle=Manzana.at[Manzana.index[cont],ColCalle]
                        auxiliarManzana=Manzana.at[Manzana.index[cont],ColIdManzana]
                        auxiliarColonia=Manzana.at[Manzana.index[cont],ColColonia]
                cont+=1
            if(len(numeros)!=0):    
                megaArreglo(CompletarNumero(min(numeros),max(numeros),auxiliarcalle,id,auxiliarColonia),megaaux)
            cont=0
            auxiliarcalle=''
            auxiliarManzana=''
            auxiliarColonia=''
            numeros=[]

SacarRangosPorCalle(calles,id)
df2 = pd.DataFrame(megaaux)
df2.to_excel ("./Mas Cercano/mamalon2.xlsx", header=True,index=False)




