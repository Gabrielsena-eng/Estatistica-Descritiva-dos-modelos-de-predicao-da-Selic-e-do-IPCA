import pandas as pd
import requests

def extrair_dados_expectativa_ipca():
    print("Baixando Expectativas do IPCA (Focus)...")
    url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativaMercadoMensais?$filter=Indicador%20eq%20'IPCA'&$orderby=Data%20desc&$top=10000&$format=json"
    response = requests.get(url)
    dados = response.json()['value']
    
    df_ipca = pd.DataFrame(dados)[['Data', 'Media']].copy()
    df_ipca.columns = ['Data', 'IPCA_Media']
    df_ipca['Data'] = pd.to_datetime(df_ipca['Data'])
    df_ipca['IPCA_Media'] = pd.to_numeric(df_ipca['IPCA_Media'], errors='coerce')
    return df_ipca.groupby('Data').mean(numeric_only=True).reset_index()

df_ipca = extrair_dados_expectativa_ipca()
print(df_ipca)

# Resumo Das informações do DataFrame
summary_stats = df_ipca['IPCA_Media'].describe()
print(summary_stats)
print(f"Primeira atualização: {df_ipca['Data'].min()} \n Ultima atualização: {df_ipca['Data'].max()}" )

