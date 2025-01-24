"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """


    import pandas as pd


    archivo_tsv = "files/input/tbl1.tsv"
    

    df = pd.read_csv(archivo_tsv, sep="\t")
    

    valores_unicos = sorted(df['c4'].str.upper().unique())
    

    return valores_unicos





if __name__ == "__main__":
    print(pregunta_06())
