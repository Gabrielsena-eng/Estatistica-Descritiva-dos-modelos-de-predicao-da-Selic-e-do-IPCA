import pandas as pd
import requests
import matplotlib.pyplot as plt


url_cotacao_dolar = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"

def extrair_dados_dolar():
    parametros = {
        '@dataInicial' : "'07-07-2025'",
        '@dataFinalCotacao' : "'07-10-2026'",
        '$format' : 'Json'
    }
    resposta = requests.get(url_cotacao_dolar, params=parametros)
    print(f"Status code : {resposta.status_code}")

    dados = resposta.json()
    df_limpo = pd.DataFrame(dados['value'])
    

    df_limpo['dataHoraCotacao'] = pd.to_datetime(df_limpo['dataHoraCotacao'])
    df_limpo = df_limpo.sort_values(by='dataHoraCotacao')

    return df_limpo


    

df_dolar_cotacao = extrair_dados_dolar()  
print(df_dolar_cotacao)


def grafico(df_limpo):
  
  plt.figure(figsize=(12, 6))
  plt.style.use('seaborn-v0_8-whitegrid')

  plt.plot(df_limpo['dataHoraCotacao'], df_limpo['cotacaoVenda'],color='red', label='Cotação Do Dolar')
  
  plt.title('Cotação do Dólar (PTAX) por Período', fontsize=14, fontweight='bold')
  plt.ylabel('Valor do Dólar (R$)', fontsize=12)
  plt.xlabel('Data', fontsize=12)
  plt.legend()
  plt.tight_layout()
  print(plt.show())

  
grafico(df_dolar_cotacao)