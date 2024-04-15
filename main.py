
from libs import *

print("\033[34m Xeli Vargas \033[0m")
archivo = input("¿Cuál es el nombre del archivo a procesar? ")


# archivo Excel
print("\033[34m Contenido del Archivo Excel :\033[0m")
wb = load_workbook(archivo)
for hoja in wb.sheetnames:
    hoja = wb[hoja]
    for row in hoja.iter_rows(values_only=True):
        print("\t".join(str(cell) for cell in row))

#  lista de relaciones
print("\n\033[34m lista relaciones :\033[0m")
matriz_adyacente = getMatriz(archivo)
for nodo, relaciones in matriz_adyacente.items():
    relaciones_str = " ".join([f"[{relacion}] : {peso} ->" for relacion, peso in relaciones.items()]) 
    print(f"Nodo {nodo} -> {relaciones_str}")


grafoTest = Grafo(archivo)
print("")
print(grafoTest)

origenG = 'B'
destinoG = 'H'
path = {}
visitados = []

visitados.append(origenG)
path[origenG] = {'-': 0}

llaves = grafoTest.Aristas[origenG].keys()

for i in llaves:
    path[i] = {origenG: grafoTest.Aristas[origenG][i]}

print(visitados)

verticeAct = 'B'
visitados.append(verticeAct)
llaves = grafoTest.Aristas[verticeAct].keys()

for i in llaves:
    if i not in visitados:
        if i not in path: path[i]={}
        llave = list(path[verticeAct].keys())
        acumulado = path[verticeAct][llave[0]]
        path[i].update({verticeAct : grafoTest.Aristas[verticeAct][i]+acumulado})

        if len(path[i]) == 2:
            kiss = list(path[i].keys())
            if kiss[0] > kiss[1]:
                del(path[i][kiss[0]])
            elif kiss[0] < kiss[1]:
                del(path[i][kiss[1]])
            pass

print(f"\033[34m path: \033[0m  {path}")
print("\033[34m cola:[#falta ]\033[0m")
print(f"\033[34m visitados\033[0m  {llaves}")