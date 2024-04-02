from .functions import *
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