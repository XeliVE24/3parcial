
import pandas as pd
from libs import *

print("\033[34m Xeli Vargas \033[0m")
archivo=input("Cual es el nombre del archivo a procesar?")

df=pd.read_excel(archivo)
print("\033[34m Matriz Adyacente :\033[0m")
print (df)



grafoTest =grafo()
origenG = 'B'
destinoG = 'H'
path ={}
visitados=[]

visitados.append(origenG)
path[origenG] = {'-':0}
llaves = grafoTest.aristas[origenG].keys()
print(llaves)

for i in llaves:
    path[i]={origenG: grafoTest.aristas[origenG][i]}

print("primer iter")
print(path)
print(visitados)



verticeAct = 'B'
llaves = grafoTest.aristas[origenG].keys()
print(llaves)

for i in llaves:
    if i not in visitados:
     #   self.aristas[origen].update((destino.peso))
        if i not in path: path[i]={}
        llave=list(path[verticeAct].keys())
        acumulado=path[verticeAct][llave[0]]
        path[i].update({verticeAct: grafoTest.aristas[verticeAct][i]+acumulado})

#revisa si hay mas de dos llaves en una llave del path
        if len(path[i]==2):
            kiss=list(path[i].keys())
            if kiss[0]>kiss[1]:
                del (path[i][kiss[0]])
            elif kiss[0]< kiss[1]:
                del(path[i][kiss[1]])
            pass
    
print(path)