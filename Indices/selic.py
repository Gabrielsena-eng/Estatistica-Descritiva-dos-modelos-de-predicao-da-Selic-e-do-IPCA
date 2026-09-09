import pandas as pd

datas_reunião = [
 
    {'Data_Vigencia': '2026-01-29', 'Reuniao': 'R1/2026'},
    {'Data_Vigencia': '2026-03-19', 'Reuniao': 'R2/2026'},
    {'Data_Vigencia': '2026-04-30', 'Reuniao': 'R3/2026'},
    {'Data_Vigencia': '2026-06-18', 'Reuniao': 'R4/2026'},
    {'Data_Vigencia': '2026-08-06', 'Reuniao': 'R5/2026'},
    {'Data_Vigencia': '2026-09-17', 'Reuniao': 'R6/2026'},
    {'Data_Vigencia': '2026-11-05', 'Reuniao': 'R7/2026'},
    {'Data_Vigencia': '2026-12-10', 'Reuniao': 'R8/2026'}
]

df_datas_reunião = pd.DataFrame(datas_reunião)
df_datas_reunião['Data_Vigencia'] = pd.to_datetime(df_datas_reunião['Data_Vigencia'])

data_inicio = '01/03/2025'
data_fim = '18/08/2026'  
url_selic = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json&dataInicial={data_inicio}&dataFinal={data_fim}'
def base_dados_selic(): 
 df_selic = pd.read_json(url_selic)
 print(df_selic)
 df_selic['data'] = pd.to_datetime(df_selic['data'], format='%d/%m/%Y')
 df_selic = df_selic.rename(columns={'data' : 'Data'})

 return df_selic

df_selic = base_dados_selic()

df_selic_resumo = pd.merge(df_datas_reunião, df_selic, left_on='Data_Vigencia', right_on='Data', how='inner' )
df_selic_resumo = df_selic_resumo.rename(columns={'valor': 'Selic_Real'})
print(df_selic_resumo)
