
import pandas as pd
from libs import *

print("\033[34m Xeli Vargas n:33 \033[0m")
archivo=input("Cual es el nombre del archivo a procesar?")

df=pd.read_excel(archivo)
print("\033[34m Matriz Adyacente :\033[0m")
print (df)