from openpyxl import load_workbook
from .classes import *


def getMatriz(archivo):
    wb = load_workbook(archivo)
    hoja = wb['Hoja1']
    filas = hoja.max_row
    columnas = hoja.max_column

    # Imprimir los datos de la hoja de cálculo
    for row in range(1, filas + 1):
        for col in range(1,columnas + 1):
            cell_value = hoja.cell(row=row, column=col).value
            print(cell_value, end='\t')  
        print()  

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


