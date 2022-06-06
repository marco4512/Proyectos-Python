import openpyxl
from cupshelpers import Printer
import pandas as pd
from regex import P
from tqdm import tqdm
import warnings
import numpy as np
print("Cargando Exel ..... (.-.)")
uno =pd.read_excel("./Mas Cercano/colonias.xlsx",engine = 'openpyxl')
dos=pd.read_excel("./Mas Cercano/localidades.xlsx",engine = 'openpyxl')
fin=pd.concat([uno,dos],ignore_index=True)
print(fin)
fin.to_excel ("./Mas Cercano/junto.xlsx", header=True,index=False)