import pandas as pd


data_inicio = '01/03/2025'
data_fim = '18/08/2026'  

def base_dados_selic(): 
    
 url_selic = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json&dataInicial={data_inicio}&dataFinal={data_fim}'
 df_selic = pd.read_json(url_selic)
 print(df_selic)
 df_selic['data'] = pd.to_datetime(df_selic['data'], format='%d/%m/%Y')
 df_selic = df_selic.rename(columns={'valor' : 'Media', 'data' : 'Data'})
 df_selic_resumo = df_selic[df_selic['Media'].diff() != 0].copy()

 return df_selic_resumo
print(base_dados_selic())