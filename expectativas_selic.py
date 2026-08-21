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

    df_limpo = df_bruto[(df_bruto['numeroRespondentes'] > 30) & 
                        (df_bruto['Reuniao'].str.contains('R4/2026')) 
                        & (df_bruto['baseCalculo'] == 0)].drop(columns=['Indicador'])
    

    df_limpo['Data'] = pd.to_datetime(df_limpo['Data'],format='%Y-%m-%d')
    df_limpo = df_limpo.sort_values(by='Data')
    return df_limpo

df_selic = extrair_dados_expectativa_selic()
print(df_selic)

summary_stats = df_selic['Media'].describe()
print(f"Summary: \n {summary_stats}")
print(f"Primeira atualização: {df_selic['Data'].min()} \n Ultima atualização: {df_selic['Data'].max()}" )

def grafico(df_limpo):
  
  plt.figure(figsize=(12, 6))
  plt.style.use('seaborn-v0_8-whitegrid')


  plt.plot(df_limpo['Data'], df_limpo['Media'], color='#1f77b4', linewidth=2, label='Expectativa Média')

  plt.fill_between(df_limpo['Data'], 
                df_limpo['Media'] - df_limpo['DesvioPadrao'], 
                df_limpo['Media'] + df_limpo['DesvioPadrao'],
                color='#1f77b4', alpha=0.2, label='Volatilidade (Desvio Padrão)')

  plt.title('Evolução das Expectativas da Selic (Reuniões de 2026)', fontsize=14, fontweight='bold')
  plt.ylabel('Taxa Selic (%)', fontsize=12)
  plt.xlabel('Data da Projeção', fontsize=12)
  plt.legend()
  plt.tight_layout()
  print(plt.show())


grafico(df_selic)
