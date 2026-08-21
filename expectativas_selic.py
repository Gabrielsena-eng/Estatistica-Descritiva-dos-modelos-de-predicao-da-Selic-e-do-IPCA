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

print(df_expectativas_agrupadas)

summary_stats = df_expectativas_selic['Media'].describe()
print(f"Summary: \n {summary_stats}")
print(f"Primeira atualização: {df_expectativas_selic['Data'].min()} \n Ultima atualização: {df_expectativas_selic['Data'].max()}" )


def grafico_evolucao_expectativas_2026(df_expectativas_bruto):
    plt.figure(figsize=(12, 6))
    
    # FILTRO NOVO: Mantém apenas as linhas onde o nome da Reunião tem "2026"
    df_2026 = df_expectativas_bruto[df_expectativas_bruto['Reuniao'].str.contains('2026', na=False)].copy()
    
    # Pega apenas as reuniões de 2026 (R1/2026, R2/2026, etc.)
    reunioes = df_2026['Reuniao'].unique()
    
    # Cria uma linha no gráfico para cada reunião de 2026
    for reuniao in reunioes:
        df_filtro = df_2026[df_2026['Reuniao'] == reuniao].copy()
        df_filtro = df_filtro.sort_values(by='Data')
        
        plt.plot(df_filtro['Data'], df_filtro['Media'], label=reuniao, linewidth=1.5)
    
    # Textos e formatação
    plt.title('Evolução Diária das Expectativas da Selic (Reuniões de 2026)', fontsize=14)
    plt.xlabel('Data da Projeção')
    plt.ylabel('Taxa Selic Esperada (%)')
    
    # Legenda para o lado de fora
    plt.legend(title='Reunião', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.5)
    plt.tight_layout()
    
    # Salva o gráfico em vetor (PDF) para o Overleaf (não perde qualidade no zoom!)
    plt.savefig('evolucao_selic_2026.pdf', format='pdf', bbox_inches='tight')
    plt.show()

# Chamada da função:
# grafico_evolucao_expectativas_2026(df_expectativas_todas)

grafico_evolucao_expectativas_2026(df_expectativas_selic)