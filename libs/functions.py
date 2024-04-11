from openpyxl import load_workbook
from .classes import *


def getMatriz(archivo):
    wb = load_workbook(archivo)
    hoja = wb['Hoja1']
    filas = hoja.max_row
    columnas = hoja.max_column

    dicc_relaciones = {}  # Diccionario para almacenar las relaciones

    for row in range(2, filas + 1):  # Empezamos desde la segunda fila ya que la primera fila contiene los nombres de los nodos
        nodo = hoja.cell(row=row, column=1).value
        dicc_relaciones[nodo] = {}  
        for col in range(2, columnas + 1):  # Empezamos desde la segunda columna ya que la primera columna contiene los nombres de los nodos
            peso = hoja.cell(row=row, column=col).value
            relacion = hoja.cell(row=1, column=col).value  
            if relacion is not None and peso != 0:  #  peso es distinto de cero
                dicc_relaciones[nodo][relacion] = peso

    return dicc_relaciones

def printDicc(dicc):
    for i in dicc:
        print(f'nodo: {i}')
        for j in dicc[i]:
            print(f'\tRel:{j},peso:{dicc[i][j]}')
        return 0 
    

class grafo():
    def __init__(self) -> None:
        self.aristas = {}
        pass
    
    def addVertice(self,vertice):
        self.aristas[vertice]={}
        pass
    
    
    #                   a       b       5
    def addArista(self,origen,destino,peso):
        if origen not in self.aristas:
            self.addVertice(origen)
        if destino not in self.aristas:
            self.addVertice(destino)
            
        # self.aristas[origen][destino] = peso
        self.aristas[origen].update({destino:peso})


    def __str__(self) -> str:
        return printDicc(self.aristas)
    pass


