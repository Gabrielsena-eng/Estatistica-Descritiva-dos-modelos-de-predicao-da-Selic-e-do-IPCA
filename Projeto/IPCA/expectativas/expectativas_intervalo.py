import pandas as pd
from pathlib import Path



from expectativas_IPCA import extrair_dados_expectativa_ipca


def extraor_intervalos_IPCA(meses, data_referencia, dias):
    df_bruto = extrair_dados_expectativa_ipca()
    df_bruto = df_bruto[df_bruto['DataReferencia'] == pd.to_datetime(data_referencia) ]
    ultima_atualizacao = df_bruto['DataReferencia'].max()

    primeira_atualizacao_intervalo = ultima_atualizacao - pd.DateOffset(months=meses)
    ultima_atualizacao_intervalo = primeira_atualizacao_intervalo + pd.DateOffset(days=dias)
    df_filtrado = df_bruto[(df_bruto['Data'] > primeira_atualizacao_intervalo) &
                            (df_bruto['Data'] < ultima_atualizacao_intervalo)]

    return df_filtrado

print(extraor_intervalos_IPCA(5, '2026-01-01', 7))

    