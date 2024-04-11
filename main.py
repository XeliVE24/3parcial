
from libs import *

print("\033[34m Xeli Vargas \033[0m")

archivo = input("¿Cuál es el nombre del archivo a procesar? ")

# archivo Excel
print("\033[34m Contenido del Archivo Excel :\033[0m")
wb = load_workbook(archivo)
for sheet in wb.sheetnames:
    hoja = wb[sheet]
    for row in hoja.iter_rows(values_only=True):
        print("\t".join(str(cell) for cell in row))

#  lista de relaciones
print("\n\033[34m lista relaciones :\033[0m")
matriz_adyacente = getMatriz(archivo)
for nodo, relaciones in matriz_adyacente.items():
    relaciones_str = ", ".join([f"[{relacion}] : {peso} ->" for relacion, peso in relaciones.items()])  # Crear una cadena de relaciones del nodo
    print(f"Nodo {nodo} -> {relaciones_str}")


"""

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
    
print(path)"""