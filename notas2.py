from openpyxl import load_workbook

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

archivo = input("¿Cuál es el nombre del archivo a procesar? ")

# Cargar y mostrar el contenido del archivo Excel
print("\033[34m Contenido del Archivo Excel :\033[0m")
wb = load_workbook(archivo)
for sheet in wb.sheetnames:
    hoja = wb[sheet]
    for row in hoja.iter_rows(values_only=True):
        print("\t".join(str(cell) for cell in row))

# Procesar la matriz adyacente y la lista de relaciones
print("\n\033[34m lista relaciones :\033[0m")
matriz_adyacente = getMatriz(archivo)
for nodo, relaciones in matriz_adyacente.items():
    relaciones_str = ", ".join([f"[{relacion}] : {peso} ->" for relacion, peso in relaciones.items()])  # Crear una cadena de relaciones del nodo
    print(f"Nodo {nodo} -> {relaciones_str}")
