import pandas as pd

from tabela_intervalos import compilar_dados_IPCA

def media_intervalos_IPCA():
 df_bruto = compilar_dados_IPCA(9)
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

print(media_intervalos_IPCA())