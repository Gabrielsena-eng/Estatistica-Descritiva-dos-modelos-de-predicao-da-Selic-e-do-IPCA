import pandas as pd


data_inicio = '01/03/2025'
data_fim = '18/08/2026'  
url_selic = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json&dataInicial={data_inicio}&dataFinal={data_fim}'
def base_dados_selic(): 
 df_selic = pd.read_json(url_selic)
 print(df_selic)
 df_selic['data'] = pd.to_datetime(df_selic['data'], format='%d/%m/%Y')
 df_selic = df_selic.rename(columns={'data' : 'Data'})
 df_selic_resumo = df_selic[df_selic['valor'].diff() != 0].copy()

 return df_selic_resumo
print(base_dados_selic())

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