import pandas as pd
import sys
from pathlib import Path
import dataframe_image as dfi

diretorio_projeto = Path(__file__).resolve().parent.parent
if str(diretorio_projeto) not in sys.path:
    sys.path.append(str(diretorio_projeto))

from intervalos.tabela_intervalos import compilar_dados_IPCA

def media_intervalos_IPCA():
 df_bruto = compilar_dados_IPCA(9)
 df_bruto['DataReferencia'] = pd.to_datetime(df_bruto['DataReferencia']).dt.strftime('%m/%Y')

 df_media = df_bruto.pivot_table(
        index=['DataReferencia', 'IPCA_Real'], 
        columns='Mes_Expectativa', 
        values='IPCA_Media', 
        aggfunc='mean'
    ).reset_index()


 df_media.columns.name = None

 
 df_media = df_media[['DataReferencia', 'IPCA_Real', 'Mes_1', 'Mes_3', 'Mes_5']]
 

 df_media['Mes_1'] = df_media['Mes_1'].round(2)
 df_media['Mes_3'] = df_media['Mes_3'].round(2)
 df_media['Mes_5'] = df_media['Mes_5'].round(2)

    
 return df_media


df_media_IPCA = media_intervalos_IPCA()
df_media_IPCA = df_media_IPCA.rename(
      columns={
         "DataReferencia": "Mês de Referência",
        "IPCA_Real": "IPCA Realizado",
        "Mes_1": "Expectativa 1 Mês",
        "Mes_3": "Expectativa 3 Meses",
        "Mes_5": "Expectativa 5 Meses",
      })
dfi.export(df_media_IPCA, "tabela_media_IPCA.png")

