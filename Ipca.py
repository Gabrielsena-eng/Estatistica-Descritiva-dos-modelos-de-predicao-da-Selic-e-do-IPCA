import pandas as pd


data_inicial = "01/03/2025"
data_final = "18/08/2026"
url_ipca = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.16122/dados?formato=json&dataInicial={data_inicial}&dataFinal={data_final}"

def base_dados_ipca():
    df_ipca = pd.read_json(url_ipca)
    print(df_ipca)


