import pandas as pd
from pathlib import Path
import sys

diretorio_projeto = Path(__file__).resolve().parent.parent
if str(diretorio_projeto) not in sys.path:
    sys.path.append(str(diretorio_projeto))

RAIZ_PROJETO = Path(__file__).resolve().parent.parent.parent
if str(RAIZ_PROJETO) not in sys.path:
    sys.path.append(str(RAIZ_PROJETO))

from IPCA.expectativas.expectativas_intervalo import extrair_intervalos_IPCA
from Indices.ipca import base_dados_ipca

def compilar_dados_IPCA (quantidade_inflacoes):
    
    lista_dfs = []
    
    for i in range(1, quantidade_inflacoes + 1):
        data_referencia = f'2026-{i:02d}-01'
        for j in range(1, 6, 2):
            df_temp = extrair_intervalos_IPCA(j, data_referencia, 7)
            df_temp['Mes_Expectativa'] = f'Mes_{j}'

            lista_dfs.append(df_temp)

    df_central = pd.concat(lista_dfs, ignore_index=True)
    df_merge = pd.merge(df_central, base_dados_ipca(), on='DataReferencia', how="left")
    df_merge = df_merge.rename(columns={ 'Media' : 'IPCA_Real'})

    return df_merge

print(compilar_dados_IPCA(9))


