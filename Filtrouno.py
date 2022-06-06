from sqlite3 import Row
import pandas as pd

print("Se lee el archivo")
df =pd.read_excel("Ejemplo.xlsx",sheet_name="Hoja1",header=0)
print("............")
print("Pasando a mayusculas")
'''Se pasa a mayusculas'''
df['DIRECCIÓN '] = df['DIRECCIÓN '].str.upper()
df['COLONIA'] = df['COLONIA'].str.upper()
df['LOCALIDAD'] = df['LOCALIDAD'].str.upper()
df['MUNICIPIO'] = df['MUNICIPIO'].str.upper()
'''Se elimian espacios atras y adelante'''
print("Eliminado espacios")
df['DIRECCIÓN '] = df['DIRECCIÓN '].str.strip()
df['COLONIA'] = df['COLONIA'].str.strip()
df['LOCALIDAD'] = df['LOCALIDAD'].str.strip()
df['MUNICIPIO'] = df['MUNICIPIO'].str.strip()
print("Reorganizando ...")
df=df.assign(CT_Estado='AGUASCALIENTES')
df = df.reindex(columns=['CT_Estado','MUNICIPIO','LOCALIDAD','COLONIA','DIRECCIÓN '])
print("Renombrando.....")
df.rename(columns={'MUNICIPIO':'CT_Municipio',
                        'LOCALIDAD':'CT_Localidad','COLONIA':'CT_Fraccionamiento','DIRECCIÓN ':'CT_Calle'},
               inplace=True)
print("ELIMINANDO Tildes")
df['CT_Municipio'] = df['CT_Municipio'].str.replace('Í', 'I')
df['CT_Municipio'] = df['CT_Municipio'].str.replace('Á', 'A')
df['CT_Municipio'] = df['CT_Municipio'].str.replace('É', 'E')
df['CT_Municipio'] = df['CT_Municipio'].str.replace('Ó', 'O')
df['CT_Municipio'] = df['CT_Municipio'].str.replace('Ú', 'U')

df['CT_Localidad'] = df['CT_Localidad'].str.replace('Í', 'I')
df['CT_Localidad'] = df['CT_Localidad'].str.replace('Á', 'A')
df['CT_Localidad'] = df['CT_Localidad'].str.replace('É', 'E')
df['CT_Localidad'] = df['CT_Localidad'].str.replace('Ó', 'O')
df['CT_Localidad'] = df['CT_Localidad'].str.replace('Ú', 'U')

df['CT_Fraccionamiento'] = df['CT_Fraccionamiento'].str.replace('Í', 'I')
df['CT_Fraccionamiento'] = df['CT_Fraccionamiento'].str.replace('Á', 'A')
df['CT_Fraccionamiento'] = df['CT_Fraccionamiento'].str.replace('É', 'E')
df['CT_Fraccionamiento'] = df['CT_Fraccionamiento'].str.replace('Ó', 'O')
df['CT_Fraccionamiento'] = df['CT_Fraccionamiento'].str.replace('Ú', 'U')
df['CT_Calle'] = df['CT_Calle'].str.replace('Í', 'I')
df['CT_Calle'] = df['CT_Calle'].str.replace('Á', 'A')
df['CT_Calle'] = df['CT_Calle'].str.replace('É', 'E')
df['CT_Calle'] = df['CT_Calle'].str.replace('Ó', 'O')
df['CT_Calle'] = df['CT_Calle'].str.replace('Ú', 'U')
df['CT_Calle'] = df['CT_Calle'].str.replace('NA', '')
df['CT_Calle'] = df['CT_Calle'].str.replace('  ', ' ')
contcel=0
contCar=0
df=df.assign(PP_numeroExterior='')
df=df.assign(PP_Interior='')
for indice in df['CT_Calle']:
    '''print("Recorriendo celda ",contcel)
    print(df.at[df.index[contcel],'CT_Calle'])'''
    contCarmenos=len(df.at[df.index[contcel],'CT_Calle'])
    num=''
    Interior=''
    direccion=''
    for indice2 in range(len(df.at[df.index[contcel],'CT_Calle'])):
        caracter = df.at[df.index[contcel],'CT_Calle']
        contCarmenos-=1
        contCarmenos2=contCarmenos
        contCarmenos3=contCarmenos2
        contCarmenos4=contCarmenos2
        PosPrimerEspacio=0
        PosPrimerEspacio2=0
        while ((caracter[contCarmenos2].isdigit())and(contCarmenos==((len(df.at[df.index[contcel],'CT_Calle']))-1))and(caracter[(contCarmenos3)-1]!=' '))  :
           
            num=num+caracter[contCarmenos2]
            contCarmenos2-=1
            
        while ((caracter[contCarmenos2]=='N')and(caracter[(contCarmenos3)-1]=='/')):
            num='N/S'
            '''print("este es",caracter[contCarmenos2])'''
            contCarmenos2-=1
        PosPrimerEspacio=len(num)
        '''while((caracter[contCarmenos2].isalpha())and(caracter[(contCarmenos3-2)].isdigit())):
            Interior=Interior+caracter[contCarmenos2]
            contCarmenos2-=1
            PosPrimerEspacio2=len(Interior)'''
    contCar-=1
        
    '''Aqui se invierte la cadena'''     
    num=num[::-1]
    Interior=Interior[::-1]

    direccion=(df.at[df.index[contcel],'CT_Calle'][0:((len(df.at[df.index[contcel],'CT_Calle']))-PosPrimerEspacio)])
   
    df.at[df.index[contcel],'CT_Calle']=str(direccion)
    df.at[df.index[contcel],'PP_numeroExterior']=num
    df.at[df.index[contcel],'PP_Interior']=Interior
    '''print(Interior)
    print(num)
    print("Numero: ",num)
    print("PrimerEspacio: ",PosPrimerEspacio)
    print("Domicilio: ",direccion)'''  
    contcel+=1
print(df)


df.to_excel ("Sedec.xlsx", header=True,index=False)
