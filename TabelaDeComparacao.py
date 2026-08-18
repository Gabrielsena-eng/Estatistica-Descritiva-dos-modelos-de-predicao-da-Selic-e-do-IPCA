import pandas as pd

from selic import base_dados_selic
from expectativas_selic import extrair_dados_expectativa_selic

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
 df_media_expectativa.rename(columns={'Media': 'media_expectativa_ciclo'}, inplace=True)
 df_media_expectativa = df_media_expectativa.drop(columns=['ciclo'])
 df_media_expectativa['Data_inicio'] = pd.to_datetime(df_media_expectativa['Data_inicio'])
 df_media_expectativa['Data_fim'] = pd.to_datetime(df_media_expectativa['Data_fim'])
 return df_media_expectativa

df_media_expectativa_selic = media_expectativa(extrair_dados_expectativa_selic(), base_dados_selic())
print(df_media_expectativa_selic)
