from glob import escape

def Completar  (min,calle):
    Digitos= len(str(min))
    esParesImpar=ParInpar(min)
    arreglofin=[]
    if(Digitos==1):
        print("uno")
        for cant in range(1,10):
            if(esParesImpar):
                if(cant % 2 == 0 ):
                    arreglofin.append([calle,cant])
            else:
                if not(cant % 2 == 0 ):
                    arreglofin.append([calle,cant])

    if(Digitos==2):
        print("Dos")
        iniciador=str(min)[0]+'0'
        for cant in range(int(iniciador),100):
            if(esParesImpar):
                if(cant % 2 == 0 ):
                    arreglofin.append([calle,cant])
            else:
                if not(cant % 2 == 0 ):
                    arreglofin.append([calle,cant])

    if(Digitos==3):
        print("Tres")
        iniciador=str(min)[0]+'00'
        for cant in range(int(iniciador),1000):
            if(esParesImpar):
                if(cant % 2 == 0 ):
                    arreglofin.append([calle,cant])
            else:
                if not(cant % 2 == 0 ):
                    arreglofin.append([calle,cant])

    if(Digitos==4):
        print("Cuatro")
        iniciador=str(min)[0]+'000'
        for cant in range(int(iniciador),10000):
            if(esParesImpar):
                if(cant % 2 == 0 ):
                    arreglofin.append([calle,cant])
            else:
                if not(cant % 2 == 0 ):
                    arreglofin.append([calle,cant])

    if(Digitos==5):
        print("Cinco")
        iniciador=str(min)[0]+'0000'
        for cant in range(int(iniciador),100000):
            if(esParesImpar):
                if(cant % 2 == 0 ):
                    arreglofin.append([calle,cant])
            else:
                if not(cant % 2 == 0 ):
                    arreglofin.append([calle,cant])
    return(arreglofin)

def ParInpar (Numero):

    if( Numero % 2 == 0 ):
        return True
    else:
        return False
    
print(Completar(10,"hola"))

