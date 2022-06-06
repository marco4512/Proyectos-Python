
import pandas as pd
from regex import P
from tqdm import tqdm
import warnings 
print("Cargando Exel ..... (.-.)")
Manzana =pd.read_excel("./Mas Cercano/PruebaOrdenada.xlsx",sheet_name="Sheet1",header=0)
CeldaMuni='NOM_MUNICI'
CeldaColonia='NOMBRE_COM'
CeldaCalle='NOMBRE_C_1'
CeldaLocali='NOM_LOCALI'
CeldaManzana='id mzna'
CeldaNumero='NUMERO_EXT'
def SacarUnicos(NombreDeLaCelda):
    """
    It takes a list of lists and returns a list of the unique elements of the lists
    
    :param NombreDeLaCelda: The name of the cell you want to get the unique values from
    :return: A list of the unique values in the column.
    """
    Aux=[]
    for celda in Manzana[NombreDeLaCelda]:
        if celda not in Aux:
            Aux.append(celda)
    return(Aux)

def soloUnos(manzana,cont):
    for celda in Manzana[CeldaManzana]:
        print(manzana,'\t',Manzana.at[Manzana.index[cont],CeldaManzana])
        if(manzana==Manzana.at[Manzana.index[cont],CeldaManzana]):
            cont+=1
        else:
            return(cont)
cont=0
def solo_recorrer_Por_Orden (Mn,cont):
    Tamaño=(len(Manzana[CeldaManzana]))
    for manzana in Mn:
        if(Tamaño>cont):
            for celda in Manzana[CeldaManzana]:
                if(Tamaño>cont):
                    if(manzana==Manzana.at[Manzana.index[cont],CeldaManzana]):
                        print('\t',Manzana.at[Manzana.index[cont],CeldaManzana])                        
                        cont+=1
                    else:
                        break
Mz=SacarUnicos(CeldaManzana)
Mn=[]
# Taking the list of unique values in the column CeldaManzana and appending to the list Mn only the
# values that are numeric.
for mnz in Mz:
    if str(mnz).isnumeric(): Mn.append(mnz)
solo_recorrer_Por_Orden(Mn,cont)




