import pandas as pd
import sys
from pathlib import Path

diretorio_projeto = Path(__file__).resolve().parent.parent
if str(diretorio_projeto) not in sys.path:
    sys.path.append(str(diretorio_projeto))

RAIZ_PROJETO = Path(__file__).resolve().parent.parent.parent
if str(RAIZ_PROJETO) not in sys.path:
    sys.path.append(str(RAIZ_PROJETO))

from expectativas.expectativas_IPCA import extrair_dados_expectativa_ipca


def extrair_intervalos_IPCA(meses, data_referencia, dias):
    df_bruto = extrair_dados_expectativa_ipca()
    df_bruto = df_bruto[df_bruto['DataReferencia'] == pd.to_datetime(data_referencia) ]
    ultima_atualizacao = df_bruto['DataReferencia'].max()

    primeira_atualizacao_intervalo = ultima_atualizacao - pd.DateOffset(months=meses)
    ultima_atualizacao_intervalo = primeira_atualizacao_intervalo + pd.DateOffset(days=dias)
    df_filtrado = df_bruto[(df_bruto['Data'] > primeira_atualizacao_intervalo) &
                            (df_bruto['Data'] < ultima_atualizacao_intervalo)]

    return df_filtrado

print(extrair_intervalos_IPCA(5, "2026-01-01", 7))





    