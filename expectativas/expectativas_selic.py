import pandas as pd
import requests
import matplotlib.pyplot as plt


url_expectativas_selic = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoSelic"

def extrair_dados_expectativa_selic():
    parametros = {
        "$format" : "json",
        "$top" : 12000
    }

    resposta = requests.get(url_expectativas_selic, params=parametros)

    print(f"Status code : {resposta.status_code}")
    dados = resposta.json()
    df_bruto = pd.DataFrame(dados['value'])

    df_limpo = df_bruto[(df_bruto['numeroRespondentes'] > 30) 
                        & (df_bruto['baseCalculo'] == 0)].drop(columns=['Indicador'])
    

    df_limpo['Data'] = pd.to_datetime(df_limpo['Data'],format='%Y-%m-%d')
    df_limpo = df_limpo.sort_values(by='Data')
    return df_limpo

df_expectativas_selic = extrair_dados_expectativa_selic()

df_expectativas_agrupadas = df_expectativas_selic.groupby('Reuniao').agg(
    Media_Historica=('Media', 'mean'),
    Desvio_Padrao_Medio=('DesvioPadrao', 'mean'),
    Qtd_Projeções=('Media', 'count')
).reset_index()


summary_stats = df_expectativas_selic['Media'].describe()
print(f"Summary: \n {summary_stats}")
print(f"Primeira atualização: {df_expectativas_selic['Data'].min()} \n Ultima atualização: {df_expectativas_selic['Data'].max()}" )


