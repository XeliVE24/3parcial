
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
listarel= getMatriz(archivo)
for nodo, relaciones in listarel.items():
    relaciones_str = " ".join([f"[{relacion}] : {peso} ->" for relacion, peso in relaciones.items()]) 
    print(f"Nodo {nodo} -> {relaciones_str}")


grafoTest = Grafo(archivo)
print("")
print("\n\033[34m GRAFO:\033[0m")
print(grafoTest)

origenG = 'B'
destinoG = 'H'
path = {}
visitados = []

visitados.append(origenG)
path[origenG] = {'-': 0}

verticeAct = 'B'

while verticeAct != destinoG:
    visitados.append(verticeAct)
    llaves = grafoTest.Aristas[verticeAct].keys()

    for i in llaves:
        if i not in visitados:
            if i not in path:
                path[i] = {}
            
            # Calcula la nueva acumulación
            llave = list(path[verticeAct].keys())
            acumulado = path[verticeAct][llave[0]]
            if grafoTest.Aristas[verticeAct][i] != 0:
                nueva_acumulacion = grafoTest.Aristas[verticeAct][i] + acumulado
                if i not in path or nueva_acumulacion < path[i].get(verticeAct, float('inf')):
                    path[i][verticeAct] = nueva_acumulacion

            

    min_peso = float('inf')
    for nodo, pesos in path.items():
        if nodo not in visitados:
            for v, p in pesos.items():
                if p < min_peso:
                    min_peso = p
                    verticeAct = nodo

camino_mas_corto = [destinoG]
vertice_actual = destinoG
peso_total = 0  
while vertice_actual != origenG:
    for v, p in path[vertice_actual].items():
        if p == min_peso:
            camino_mas_corto.append(v)
            peso_total += grafoTest.Aristas[v][vertice_actual]  # Sumamos el peso de la arista al peso total
            min_peso -= grafoTest.Aristas[v][vertice_actual]
            vertice_actual = v
            break
camino_mas_corto.reverse()

print(f"\033[34m path:\033[0m{path}")
print(f"\033[34m visitados:\033[0m {visitados}")
print(f"\033[34m El camino más corto es:\033[0m", camino_mas_corto)
print(f"\033[34m Peso total : \033[0m {peso_total}")
