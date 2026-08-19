import pandas as pd
import requests

data_inicial_filtro = "2025-03-01"

def extrair_dados_expectativa_ipca():
    print("Baixando Expectativas do IPCA (Focus)...")
    url = f"https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativaMercadoMensais?$filter=Indicador%20eq%20'IPCA'%20and%20Data%20ge%20'{data_inicial_filtro}'&$orderby=Data%20asc&$top=10000&$format=json"
    response = requests.get(url)
    dados = response.json()['value']
    
    df_ipca = pd.DataFrame(dados)[['Data', 'Media', 'DataReferencia']].copy()
    df_ipca.columns = ['Data', 'IPCA_Media','DataReferencia']
    df_ipca['Data'] = pd.to_datetime(df_ipca['Data'])
    df_ipca['DataReferencia'] = pd.to_datetime(df_ipca['DataReferencia'], format="%m/%Y")
    df_ipca['IPCA_Media'] = pd.to_numeric(df_ipca['IPCA_Media'], errors='coerce')
    df_ipca = df_ipca.rename(columns={'IPCA_Media' : 'Media'})
    return df_ipca

df_ipca = extrair_dados_expectativa_ipca()
print(df_ipca)

# Resumo Das informações do DataFrame





def alinhar_dados_ipca():
    df_filtrado = df_ipca[(df_ipca['DataReferencia'] >= '2025-03-01') & 
                          (df_ipca['DataReferencia'] <= '2026-09-01')].copy()
    df_filtrado = df_filtrado.drop(columns='Data')
    df_filtrado = df_filtrado.rename(columns={'DataReferencia' : 'Data'})
    
    return df_filtrado

df_ipca_ordenado = alinhar_dados_ipca()
print(df_ipca_ordenado)

print(f"Primeira atualização: {df_ipca_ordenado['Data'].min()} \n Ultima atualização: {df_ipca_ordenado['Data'].max()}" )
summary_stats = df_ipca_ordenado['Media'].describe()
print(summary_stats)