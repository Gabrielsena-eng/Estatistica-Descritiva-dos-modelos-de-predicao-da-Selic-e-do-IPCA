import pandas as pd

from selic import df_selic_resumo
from expectativas_selic import df_expectativas_agrupadas
from ipca import base_dados_ipca
from expectativas_IPCA import extrair_dados_expectativa_ipca
from expectativas_IPCA import alinhar_dados_ipca

def media_expectativa(df_expectativa, df_real):
 bins = df_real['Data'].tolist()

 df_expectativa['ciclo'] = pd.cut(
  df_expectativa['Data'],
  bins=bins,
  include_lowest=True,
  right=False
 )

 df_media_expectativa = df_expectativa.groupby('ciclo')['Media'].mean().reset_index()
 df_media_expectativa['ciclo'] = df_media_expectativa['ciclo'].astype(str)
 df_media_expectativa['ciclo'] = df_media_expectativa['ciclo'].str.strip('[]()')
 df_media_expectativa[['Data_inicio', 'Data_fim']] = df_media_expectativa['ciclo'].str.split(', ', n=1, expand=True)

 df_media_expectativa.rename(columns={'Media': 'media_expectativa_ciclo', 'Data_inicio' : 'Data'}, inplace=True)
 df_media_expectativa = df_media_expectativa.drop(columns=['ciclo', 'Data_fim'])

 df_media_expectativa['Data'] = pd.to_datetime(df_media_expectativa['Data'])

 
 return df_media_expectativa

df_media_expectativa_ipca = media_expectativa(alinhar_dados_ipca(), base_dados_ipca())



def mesclagem_dataframes(df_media_expectativa, df_media_real):
   df_comparacao = pd.merge(
    df_media_expectativa,
    df_media_real,
    on='Data',
    how='inner'
  )
   df_comparacao = df_comparacao.rename(columns={'Media' : 'Valor_Real',
                                                'media_expectativa_ciclo' : 'Valor_esperado'})
   df_comparacao['Erro'] = df_comparacao['Valor_Real'] - df_comparacao['Valor_esperado']
   df_comparacao = df_comparacao[['Data', 'Valor_esperado', 'Valor_Real', 'Erro']]
   df_comparacao = df_comparacao.sort_values(by='Data').reset_index(drop=True)
   
   return df_comparacao

df_comparacao_selic = pd.merge(df_selic_resumo, df_expectativas_agrupadas, on='Reuniao', how='inner')
df_comparacao_selic['Erro_Medio'] = df_comparacao_selic['Media_Historica'] - df_comparacao_selic['Selic_Real']
df_comparacao_selic = df_comparacao_selic.sort_values(by='Data_Vigencia')
print(df_comparacao_selic)
df_comparacao_ipca = mesclagem_dataframes(df_media_expectativa_ipca, base_dados_ipca())


