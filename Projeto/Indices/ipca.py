import pandas as pd


data_inicial = "01/03/2025"
data_final = "18/08/2026"
url_ipca = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.16122/dados?formato=json&dataInicial={data_inicial}&dataFinal={data_final}"

def base_dados_ipca():
    df_ipca = pd.read_json(url_ipca)
    df_ipca['data'] = pd.to_datetime(df_ipca['data'], format='%d/%m/%Y')
    df_ipca = df_ipca.rename(columns={'data': 'Data', 'valor' : 'Media'})
    df_ipca['Media'] = df_ipca['Media']

    return df_ipca

df_ipca = base_dados_ipca()
print(df_ipca)


