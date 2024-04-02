from .classes import *

def printDicc(dicc):
    for i in dicc:
        print(f'nodo: {i}')
        for j in dicc[i]:
            print(f'\tRel:{j},peso:{dicc[i][j]}')
        return 0 
    


