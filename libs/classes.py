from .functions import *

class Grafo:
    def __init__(self, archivo) -> None:
        self.Aristas = self.Excel(archivo)
    
    def Excel(self, archivo):
        df = pd.read_excel(archivo, index_col=0)
        return df.to_dict(orient='index')
    
    def addVertice(self, vertice):
        if vertice not in self.Aristas:
            self.Aristas[vertice] = {}
    
    def addArista(self, origen, destino, peso):
        self.addVertice(origen)
        self.addVertice(destino)
        self.Aristas[origen][destino] = peso
    
    def __str__(self) -> str:
        return self.printDicc(self.Aristas)

    def printDicc(self, dicc):
        result = ""
        for i in dicc:
            result += f'nodo: {i}\n'
            for j in dicc[i]:
                result += f'\tDestino:{j},peso:{dicc[i][j]}\n'
        return result




