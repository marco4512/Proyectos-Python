import os
from typing import Literal


def borrar():
    Dir = "./DivicionCentro/htmls"
    Lista = os.listdir(Dir)
    print(Lista)

    for e in Lista:
        print(e, "->",e.endswith(".html"))
        if(e.endswith(".html")):
            os.remove(Dir+"/"+e)
    for e in Lista:
        print(e, "->",e.endswith(".html"))
    
borrar()