from fileinput import filename
from tkinter import *
from tkinter import filedialog
from numpy import place 
import pandas as pd
from tqdm import tqdm
import time 
import sys

 

filename=''
def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Selecciona el archivo", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
       
    
    label_file_explorer.configure(text="File Opened: "+filename)

    df =pd.read_excel(filename,sheet_name="Hoja1",header=0)
 
    '''Se pasa a mayusculas'''
    df['CT_Calle'] = df['CT_Calle'].str.upper()
    df['CT_Fraccionamiento'] = df['CT_Fraccionamiento'].str.upper()
    df['CT_Localidad'] = df['CT_Localidad'].str.upper()
    df['CT_Municipio'] = df['CT_Municipio'].str.upper()
    '''Se elimian espacios atras y adelante'''

    df['CT_Calle'] = df['CT_Calle'].str.strip()
    df['CT_Fraccionamiento'] = df['CT_Fraccionamiento'].str.strip()
    df['CT_Localidad'] = df['CT_Localidad'].str.strip()
    df['CT_Municipio'] = df['CT_Municipio'].str.strip()

    df=df.assign(CT_Estado='AGUASCALIENTES')
    df = df.reindex(columns=['CT_Estado','CT_Municipio','CT_Localidad','CT_Fraccionamiento','CT_Calle'])
   
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
    df['CT_Calle'] = df['CT_Calle'].str.replace('-', ' ')
    df['CT_Calle'] = df['CT_Calle'].str.replace('NA', '')
    df['CT_Calle'] = df['CT_Calle'].str.replace('SN', 'S/N')
    df['CT_Calle'] = df['CT_Calle'].str.replace('  ', ' ')
    df=df.assign(PP_numeroExterior='')
    df=df.assign(PP_Interior='')
    contcel=0
    contvac=0
    caracter=''
    contCarmenos=0
    cont=0
    cont2=0
    df['PP_numeroExterior'].fillna('null', inplace=True)
    df['CT_Calle'].fillna('null', inplace=True)
    df['CT_Calle'] = df['CT_Calle'].str.strip()
    for indice in tqdm(range(int(len(df['CT_Calle'])))):
        contCarmenos=df.at[df.index[contcel],'CT_Calle']
        contCarmenos=len(str(contCarmenos))
        num=''
        PosPrimerEspacio=0
        direccion=''
        if(df.at[df.index[contcel],'PP_numeroExterior']=='null'):
            for indice2 in range(len(df.at[df.index[contcel],'CT_Calle'])):
                caracter = df.at[df.index[contcel],'CT_Calle']
                cont+=1
                contCarmenos-=1
            cont2=(cont-1)
            cont3=cont2+1
            cont4=cont3+1
            for indice3 in range(len(df.at[df.index[contcel],'CT_Calle'])):
                cont3-=1
                
                while((caracter[cont2].isdigit())and(caracter[cont3]!=' ')):
                    
                    num=num+caracter[cont2]
                    cont2-=1
                while ((caracter[cont2]=='N')and(caracter[cont3]=='/')):
                    num='N/S'
                    '''print("este es",caracter[contCarmenos2])'''
                    cont2-=1
                    PosPrimerEspacio=len(num)
            cont=0
        PosPrimerEspacio=len(num)
        
        num=num[::-1]
        Ultimo=len((str(df.at[df.index[contcel],'CT_Calle'])))
        Ultimo=Ultimo-PosPrimerEspacio
        direccionAux=str(df.at[df.index[contcel],'CT_Calle'])
        direccion=direccionAux[0:Ultimo]    
        '''print("Num: ",num)
        print("Calle: ",direccion)'''
        if(df.at[df.index[contcel],'PP_numeroExterior']=='null'):
            df.at[df.index[contcel],'CT_Calle']=str(direccion)
            df.at[df.index[contcel],'PP_numeroExterior']=str(num)
        contcel+=1
        pass    
  
    df.to_excel ("./temp/Sedec.xlsx", header=True,index=False)
   
    exec(open("NumeroInterno.py").read())
    exec(open("Caso1.py").read())
    print("------Fin-----")
    
    
   
       
                                                                                                   
window = Tk() 
   
window.title('Filtrador de Numero y Calle') 
   
window.geometry("805x120") 
   
window.config(background = "#2471A3") 
   
label_file_explorer = Label(window,  
                            text = "Para filtar Ingresa la direccion de tu archivo", 
                            width = 100, height = 4,  
                            fg = "white",
                            background = "#17202A") 
   
       
button_explore = Button(window,  
                        text = "Buscar Archivo", 
                        command = browseFiles
                        )
   
button_exit = Button(window,  
                     text = "Exit", 
                     command = exit)  
   
label_file_explorer.grid(column = 1, row = 1) 
   
button_explore.place(x=300,y=80)
   
button_exit.place(x=450,y=80)

   
window.mainloop() 
