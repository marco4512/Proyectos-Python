from traceback import print_tb
import pandas as pd
from tqdm import tqdm
def undigito(numero,lista):
    str_numero = str(numero)
    uno=[n for n in lista if n<10]
    if (len(uno)>=1):
        if (numero % 2 == 0):
            uno_par = [n for n in uno if n % 2 == 0]
            if(len(uno_par)>=1):
                lista_final = []
                for n in uno_par:
                    if (numero < n):
                        lista_final.append(n - numero)
                    else:
                        lista_final.append(numero - n)
                indice = min(lista_final)
                indice = lista_final.index(indice)
                
                return uno_par[indice]
            else: 
                return 0

        else:
            uno_impar = [n for n in uno if n % 2 != 0]
            if(len(uno_impar)>=1):
                lista_final = []
                for n in uno_impar:
                    if (numero < n):
                        lista_final.append(n - numero)
                    else:
                        lista_final.append(numero - n)
                indice = min(lista_final)
                indice = lista_final.index(indice)
            
                return uno_impar[indice]
            else:
                return 0
    else: 
        return 0 

def dos_digitos(numero,lista):
    str_numero=str(numero)
    digito_uno=str_numero[0]
    dos = [n for n in lista if n < 100 and n >= 10]
    if(numero%2==0):
        dos_par=[n for n in dos if n%2==0]
      
        lista_uno=[]
        for i in dos_par:
            aux=str(i)
            if digito_uno==aux[0]:
                lista_uno.append(i)
        if(len(lista_uno)>=1):
            
            lista_final = []
            for n in lista_uno:
                if (numero < n):
                    lista_final.append(n - numero)
                else:
                    lista_final.append(numero - n)
            indice = min(lista_final)
            indice = lista_final.index(indice)
           
            return lista_uno[indice]
        else:
           
            return 0
    else:
        dos_impar=[n for n in dos if n%2!=0]
       
        lista_uno = []
        for i in dos_impar:
            aux = str(i)
            if digito_uno == aux[0]:
                lista_uno.append(i)
        if (len(lista_uno) >= 1):
    
            lista_final = []
            for n in lista_uno:
                if (numero < n):
                    lista_final.append(n - numero)
                else:
                    lista_final.append(numero - n)
            indice = min(lista_final)
            indice = lista_final.index(indice)
           
            return lista_uno[indice]
            
        else:
            
            return 0

def tres_digito(numero,lista):
    str_numero=str(numero)
    digito_uno=str_numero[0]
    digito_dos = str_numero[1]
    tres = [n for n in lista if n <=999 and n >= 100]
    if numero%2==0:
        tres_par=[n for n in tres if n%2==0]
      
        lista_uno=[]
        for i in tres_par:
            aux=str(i)
            if digito_uno== aux[0]:
                lista_uno.append(i)
        if len(lista_uno)>=1:
           
            lista_dos=[]
            for i in lista_uno:
                aux = str(i)
                if digito_dos == aux[1]:
                    lista_dos.append(i)
            
            if(len(lista_dos)>=1):
                lista_final = []
                for n in lista_dos:
                    if (numero < n):
                        lista_final.append(n - numero)
                    else:
                        lista_final.append(numero - n)
                indice = min(lista_final)
                indice = lista_final.index(indice)
               
                return lista_dos[indice]
            else:
               
                return 0
        else:
           
            return 0
    else:
        tres_impar = [n for n in tres if n % 2 != 0]
   
        lista_uno = []
        for i in tres_impar:
            aux = str(i)
            if digito_uno == aux[0]:
                lista_uno.append(i)
   
        lista_dos = []
        for i in lista_uno:
            aux = str(i)
            if digito_dos == aux[1]:
                lista_dos.append(i)
     
        if (len(lista_dos) >= 1):
            lista_final = []
            for n in lista_dos:
                if (numero < n):
                    lista_final.append(n - numero)
                else:
                    lista_final.append(numero - n)
            indice = min(lista_final)
            indice = lista_final.index(indice)
           
            return lista_dos[indice]
        else:
       
            return 0
def cuatro_digito(numero,lista):
    str_numero = str(numero)
    
    digito_uno = str_numero[0]
    digito_dos = str_numero[1]
    digito_tres = str_numero[2]
    cuatro = [n for n in lista if n <= 9999 and n >= 1000]
    #print(cuatro)
    if numero%2==0:
        tres_par=[n for n in cuatro if n%2==0]
       
        lista_uno=[]
        for i in tres_par:
            aux=str(i)
            if digito_uno== aux[0]:
                lista_uno.append(i)
        if len(lista_uno)>=1:
            lista_dos=[]
            for i in lista_uno:
                aux = str(i)
                if digito_dos == aux[1]:
                    lista_dos.append(i)
     
            if(len(lista_dos)>=1):

             
                lista_tres=[]
                for i in lista_dos:
                    aux = str(i)
                    if digito_tres == aux[2]:
                        lista_tres.append(i)
                if(len(lista_tres)>=1):

                  
                    lista_final = []
                   
                    for n in lista_tres:
                        if (numero < n):
                            lista_final.append(n - numero)
                        else:
                            lista_final.append(numero - n)
                   
                    indice = min(lista_final)
                    
                    indice = lista_final.index(indice)
                    
                    return lista_tres[indice]
                else:
                    
                    return 0
            else:
               
                return 0
        else:
            
            return 0
    else:
        tres_impar = [n for n in cuatro if n % 2 != 0]
      
        lista_uno = []
        for i in tres_impar:
            aux = str(i)
            if digito_uno == aux[0]:
                lista_uno.append(i)
        if len(lista_uno) >= 1:

       
            lista_dos = []
            for i in lista_uno:
                aux = str(i)
                if digito_dos == aux[1]:
                    lista_dos.append(i)
          
            if (len(lista_dos) >= 1):

                lista_tres = []
                for i in lista_dos:
                    aux = str(i)
                    if digito_tres == aux[2]:
                        lista_tres.append(i)
                if (len(lista_tres) >= 1):
                 
                    lista_final = []
                    for n in lista_tres:
                        if (numero < n):
                            lista_final.append(n - numero)
                        else:
                            lista_final.append(numero - n)
                    indice = min(lista_final)
                    indice = lista_final.index(indice)
                   
                    return lista_tres[indice]
                else:
                   
                    return 0
            else:
                
                return 0
        else:
           
            return 0

def cinco_digito(numero,lista):
    cinco = [n for n in lista if n <= 99999 and n >= 10000]
    str_numero = str(numero)
    digito_uno = str_numero[0]
    digito_dos = str_numero[1]
    digito_tres = str_numero[2]
    digito_cuatro = str_numero[3]
    # print(cuatro)
    if numero % 2 == 0:
        cinco_par = [n for n in cinco if n % 2 == 0]
     
        lista_uno = []
        for i in cinco_par:
            aux = str(i)
            if digito_uno == aux[0]:
                lista_uno.append(i)
        if len(lista_uno) >= 1:

           
            lista_dos = []
            for i in lista_uno:
                aux = str(i)
                if digito_dos == aux[1]:
                    lista_dos.append(i)
            
            if (len(lista_dos) >= 1):
              
                lista_tres = []
                for i in lista_dos:
                    aux = str(i)
                    if digito_tres == aux[2]:
                        lista_tres.append(i)
                if (len(lista_tres) >= 1):
                 
                    lista_cuatro = []
                    for n in lista_tres:
                        aux = str(i)
                        if digito_cuatro == aux[3]:
                            lista_cuatro.append(n)
                    if(len(lista_cuatro)>=1):
                        lista_final = []
                        for n in lista_cuatro:
                            if (numero < n):
                                lista_final.append(n - numero)
                            else:
                                lista_final.append(numero - n)
                        indice = min(lista_final)
                        indice = lista_final.index(indice)
                        
                        return lista_cuatro[indice]
                else:
                
                    return 0
        else:
           
            return 0
    else:
        cinco_impar = [n for n in cinco if n % 2 != 0]
       
        lista_uno = []
        for i in cinco_impar:
            aux = str(i)
            if digito_uno == aux[0]:
                lista_uno.append(i)
        if len(lista_uno) >= 1:

    
            lista_dos = []
            for i in lista_uno:
                aux = str(i)
                if digito_dos == aux[1]:
                    lista_dos.append(i)
           
            if (len(lista_dos) >= 1):
               
                lista_tres = []
                for i in lista_dos:
                    aux = str(i)
                    if digito_tres == aux[2]:
                        lista_tres.append(i)
                if (len(lista_tres) >= 1):
                   
                    lista_cuatro = []
                    for n in lista_tres:
                        aux = str(i)
                        if digito_cuatro == aux[3]:
                            lista_cuatro.append(n)
                    if (len(lista_cuatro) >= 1):
                        lista_final = []
                        for n in lista_cuatro:
                            if (numero < n):
                                lista_final.append(n - numero)
                            else:
                                lista_final.append(numero - n)
                        indice = min(lista_final)
                        indice = lista_final.index(indice)
                        return lista_cuatro[indice]
                else:
                    
                    return 0
        else:
            return 0
print("Cargando Exel ..... (.-.)")
NoCorrectos =pd.read_excel("./Mas Cercano/FiltradoIncorrectos.xlsx",sheet_name="Sheet1",header=0)
GeneralFiltrado =pd.read_excel("./Mas Cercano/Ejemplo2.xlsx",sheet_name="Sheet1",header=0)
Fraccionamientos=[]
print("Cargando Fraccionamientos    Unicos ..... (+*+)")
NoCorrectos=NoCorrectos.assign(OBJECTID='')

for fraccionamiento in tqdm(NoCorrectos['frac catastro']):
    if fraccionamiento not in Fraccionamientos:
        Fraccionamientos.append(fraccionamiento)
dicFraCalle={}
ct=0
Aux=[]
NoCorrectos['frac catastro'].fillna('N/A', inplace=True)
print("Creando Diccionario ..... (.*.)")
for fracc in  tqdm(Fraccionamientos):
    for calle in GeneralFiltrado['NOMBRE_COM']:
        if (str(calle).count(str(fracc))==1):
            Aux.append([GeneralFiltrado.at[GeneralFiltrado.index[ct],'NOMBRE_C_1'],GeneralFiltrado.at[GeneralFiltrado.index[ct],'ext_1'],GeneralFiltrado.at[GeneralFiltrado.index[ct],'OBJECTID']])
        ct+=1
    dicFraCalle[fracc]=[Aux]
    Aux=[]
    ct=0
NumCalle=[]
AxNumCalle=[]
Par=[]
Impar=[]
cn=0
for Col in tqdm(NoCorrectos['frac catastro']):
    numEncontrar=NoCorrectos.at[NoCorrectos.index[cn],'PP_numeroExterior']
    calleNo=str(NoCorrectos.at[NoCorrectos.index[cn],'calle catastro'])
    for CalleGeneral in dicFraCalle[str(NoCorrectos.at[NoCorrectos.index[cn],'frac catastro'])][0]:
        if (calleNo.count(str(CalleGeneral[0]))):
            NumCalle.append([CalleGeneral[1],CalleGeneral[2]])
            AxNumCalle.append(int(CalleGeneral[1]))
    numEncontrar=int(numEncontrar)
    digitos=len(str(numEncontrar))
    if(len(AxNumCalle)!=0):
        if digitos==1:
            
            numcercano=undigito(int(numEncontrar),AxNumCalle)
            if(numcercano!=0):
                for aEncontrrar in NumCalle:
                    if(int(aEncontrrar[0])==numcercano):
                        NoCorrectos.at[NoCorrectos.index[cn],'OBJECTID']=aEncontrrar[1]
            else:
                NoCorrectos.at[NoCorrectos.index[cn],'OBJECTID']="No Cercano"
        if digitos==2:
            numcercano=dos_digitos(int(numEncontrar),AxNumCalle)
            if(numcercano!=0):
                for aEncontrrar in NumCalle:
                    if(int(aEncontrrar[0])==numcercano):
                        NoCorrectos.at[NoCorrectos.index[cn],'OBJECTID']=aEncontrrar[1]
            else:
                NoCorrectos.at[NoCorrectos.index[cn],'OBJECTID']="No Cercano"
        if digitos==3:
            numcercano=tres_digito(int(numEncontrar),AxNumCalle)
            if(numcercano!=0):
                for aEncontrrar in NumCalle:
                    if(int(aEncontrrar[0])==numcercano):
                        NoCorrectos.at[NoCorrectos.index[cn],'OBJECTID']=aEncontrrar[1]
            else:
                NoCorrectos.at[NoCorrectos.index[cn],'OBJECTID']="No Cercano"
        if digitos==4:
            numcercano=cuatro_digito(int(numEncontrar),AxNumCalle)
            if(numcercano!=0):
                for aEncontrrar in NumCalle:
                    if(int(aEncontrrar[0])==numcercano):
                        NoCorrectos.at[NoCorrectos.index[cn],'OBJECTID']=aEncontrrar[1]
            else:
                NoCorrectos.at[NoCorrectos.index[cn],'OBJECTID']="No Cercano"
        if digitos==5:
            numcercano=cinco_digito(int(numEncontrar),AxNumCalle)
            if(numcercano!=0):
                for aEncontrrar in NumCalle:
                    if(int(aEncontrrar[0])==numcercano):
                        NoCorrectos.at[NoCorrectos.index[cn],'OBJECTID']=aEncontrrar[1]
            else:
                NoCorrectos.at[NoCorrectos.index[cn],'OBJECTID']="No Cercano"
    '''for ParInpar in NumCalle:
        if (int(ParInpar[0]))%2 == 0:
            if ParInpar[0] not in Par: 
                Par.append([ParInpar[0],ParInpar[1]])
        else:
            if ParInpar[0] not in Impar:
                Impar.append([ParInpar[0],ParInpar[1]])'''
    
    NumCalle=[]
    AxNumCalle=[]
    Par=[]
    Impar=[]
    cn+=1
NoCorrectos.to_excel ("./Mas Cercano/LosChidos.xlsx", header=True,index=False)