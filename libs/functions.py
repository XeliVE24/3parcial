from openpyxl import load_workbook
import pandas as pd 

def getMatriz(archivo):
    wb = load_workbook(archivo)
    hoja = wb['Hoja1']
    filas = hoja.max_row
    columnas = hoja.max_column

    dicc_relaciones = {}
    for row in range(2, filas + 1):
        nodo = hoja.cell(row=row, column=1).value
        dicc_relaciones[nodo] = {}
        for col in range(2, columnas + 1):
            peso = hoja.cell(row=row, column=col).value
            relacion = hoja.cell(row=1, column=col).value
            if relacion is not None and peso != 0:
                dicc_relaciones[nodo][relacion] = peso

    return dicc_relaciones

  
