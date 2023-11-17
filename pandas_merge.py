"""
Mezcla de ficheros csv utilizando un campo clave: inner join
"""
import pandas as pd

path = "../curso_csic_2023-main/practicas/pandas/merge/"

dfEmpresas = pd.read_csv(path+"Empresas.txt", sep=";")
dfEmpleados = pd.read_csv(path+"Empleados.txt", sep=";")
dfPedidos = pd.read_csv(path+"Pedidos.txt", sep=";")

dfFinal = pd.merge(dfPedidos, dfEmpresas, left_on='idempresa', right_on="id")
print(dfFinal.head(3))
dfFinal = pd.merge(dfFinal, dfEmpleados, left_on="idempleado",right_on="id")
print(dfFinal.columns)

# borrar cols del DataFrame:
dfFinal.drop(columns=['id_x','id_y','cargo','idempresa','idempleado'], \
             inplace=True)
# Renombrar cols: dict {col_old: col_new}
dfFinal.rename(columns={"nombre":"empleado"}, inplace=True)
dfFinal.to_excel(path+"final.xlsx", index=False)