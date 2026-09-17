import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from Projeto.TabelaDeComparacao import df_comparacao_selic
from Projeto.TabelaDeComparacao import df_comparacao_ipca
from Projeto.IPCA.expectativas.expectativas_IPCA import alinhar_dados_ipca
from Projeto.SELIC.expectativas.expectativas_selic import extrair_dados_expectativa_selic
from Projeto.IPCA.expectativas.expectativas_IPCA import extrair_dados_expectativa_ipca
from Projeto.SELIC.expectativas.expectativas_selic import df_expectativas_selic


import matplotlib.pyplot as plt
import pandas as pd

def plotar_barras_ipca_2026(df_comparacao_ipca):
    df_2026 = df_comparacao_ipca[df_comparacao_ipca['Data'].dt.year == 2026].copy()
    

    df_2026 = df_2026.sort_values(by='Data')

    df_2026['Data_str'] = df_2026['Data'].dt.strftime('%Y-%m')
    
 
    df_2026 = df_2026.rename(columns={
        'Media_Expectativa': 'Valor_esperado',
        'IPCA_Real': 'Valor_Real'
    })
    

    fig, ax = plt.subplots(figsize=(12, 6))
    
    df_2026.plot(
        x='Data_str',
        y=['Valor_esperado', 'Valor_Real'],
        kind='bar',
        ax=ax,
        color=['#1f77b4', '#d62728'], 
        width=0.8
    )
    

    ax.set_title('IPCA 2026: Expectativa do Mercado vs Realidade', fontsize=14, fontweight='bold')
    ax.set_ylabel('Variação Mensal do IPCA (%)', fontsize=12)
    ax.set_xlabel('Mês de Referência', fontsize=12)
    

    plt.xticks(rotation=0, ha='center') 
    plt.legend(['Expectativa (Mercado)', 'Realidade (BCB)'])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    

    
    plt.show()
 


plotar_barras_ipca_2026(df_comparacao_ipca)


def plotar_estatisticas_distribuicao(df_ipca, df_selic):
    
    sns.set_theme(style="whitegrid")
    
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    sns.histplot(df_ipca['Media'], kde=True, ax=axes[0], color='#1f77b4', bins=30)
    axes[0].set_title('Distribuição: Expectativas IPCA', fontsize=12, fontweight='bold')
    axes[0].set_xlabel('Taxa IPCA (%)', fontsize=10)
    axes[0].set_ylabel('Frequência', fontsize=10)
    
    sns.histplot(df_selic['Media'], kde=True, ax=axes[1], color='#2ca02c', bins=30)
    axes[1].set_title('Distribuição: Expectativas Selic', fontsize=12, fontweight='bold')
    axes[1].set_xlabel('Taxa Selic (%)', fontsize=10)
    axes[1].set_ylabel('Frequência', fontsize=10)
    
    plt.tight_layout()
    plt.show()
    
    
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    sns.boxplot(y=df_ipca['Media'], ax=axes[0], color='#1f77b4')
    axes[0].set_title('Boxplot: Expectativas IPCA', fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Taxa IPCA (%)', fontsize=10)
    
    sns.boxplot(y=df_selic['Media'], ax=axes[1], color='#2ca02c')
    axes[1].set_title('Boxplot: Expectativas Selic', fontsize=12, fontweight='bold')
    axes[1].set_ylabel('Taxa Selic (%)', fontsize=10)
    
    plt.tight_layout()
    plt.show()

plotar_estatisticas_distribuicao(alinhar_dados_ipca(), extrair_dados_expectativa_selic())



def plotar_barras_selic(df):
    # Usar 'Reuniao' como índice facilita criar as barras agrupadas no pandas
    df_plot = df.set_index('Reuniao')
    
    # Selecionamos apenas as duas colunas que queremos comparar
    df_plot = df_plot[['Media_Historica', 'Selic_Real']]
    
    # Renomeamos as colunas apenas no df_plot para a legenda do gráfico ficar bonita
    df_plot = df_plot.rename(columns={
        'Media_Historica': 'Expectativa (Média)',
        'Selic_Real': 'Realidade (BCB)'
    })
    
    # Cria a figura e plota
    fig, ax = plt.subplots(figsize=(12, 6))
    df_plot.plot(
        kind='bar', 
        ax=ax, 
        color=['#1f77b4', '#d62728'], 
        width=0.7
    )
    
    # Ajustes visuais
    ax.set_title('Expectativa do Mercado vs Selic Realizada', fontsize=14, fontweight='bold')
    ax.set_ylabel('Taxa Selic (%)', fontsize=12)
    ax.set_xlabel('Reunião', fontsize=12)
    
    plt.xticks(rotation=0) # Deixa o texto R1/2026, R2/2026 na horizontal
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend(loc='upper right')
    
    plt.tight_layout()
    plt.show()

# Chama a função passando exatamente o seu DataFrame
plotar_barras_selic(df_comparacao_selic)


def grafico_linha_simples(df):
    plt.figure(figsize=(10, 5))
    
    # Plota as duas linhas
    plt.plot(df['Reuniao'], df['Selic_Real'], marker='o', color='red', label='Selic Real')
    plt.plot(df['Reuniao'], df['Media_Historica'], marker='s', color='blue', label='Expectativa (Média)')
    
    # Textos e legendas básicos
    plt.title('Evolução: Selic Real vs Expectativa do Mercado', fontsize=14)
    plt.xlabel('Reunião')
    plt.ylabel('Taxa Selic (%)')
    plt.legend()
    plt.grid(True, alpha=0.5)
    
    plt.tight_layout()
    plt.show()


grafico_linha_simples(df_comparacao_selic)



# Adicionei o df_realizado como segundo parâmetro para saber quais reuniões já passaram
def grafico_evolucao_expectativas_2026(df_expectativas_bruto, df_realizado):
    plt.figure(figsize=(12, 6))
    
    # 1. Pega a lista exata de reuniões que já têm a Selic Real (ex: ['R1/2026', 'R2/2026', ...])
    reunioes_passadas = df_realizado['Reuniao'].unique()
    
    # 2. FILTRO DUPLO: Mantém apenas as linhas de 2026 E que estejam na lista de reuniões que já aconteceram
    df_2026 = df_expectativas_bruto[
        (df_expectativas_bruto['Reuniao'].str.contains('2026', na=False)) &
        (df_expectativas_bruto['Reuniao'].isin(reunioes_passadas))
    ].copy()
    
    # Pega apenas as reuniões de 2026 filtradas
    reunioes = df_2026['Reuniao'].unique()
    
    # Cria uma linha no gráfico para cada reunião
    for reuniao in reunioes:
        df_filtro = df_2026[df_2026['Reuniao'] == reuniao].copy()
        df_filtro = df_filtro.sort_values(by='Data')
        
        plt.plot(df_filtro['Data'], df_filtro['Media'], label=reuniao, linewidth=1.5)
    
    # Textos e formatação
    plt.title('Evolução Diária das Expectativas (Apenas Reuniões Realizadas de 2026)', fontsize=14)
    plt.xlabel('Data da Projeção')
    plt.ylabel('Taxa Selic Esperada (%)')
    
    # Legenda para o lado de fora
    plt.legend(title='Reunião', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.5)
    plt.tight_layout()
    
    # Salva o gráfico em vetor (PDF) para o Overleaf
    plt.savefig('evolucao_selic_2026.pdf', format='pdf', bbox_inches='tight')
    plt.show()

# Chamada da função passando as expectativas brutas e a tabela de comparação (que tem os dados reais):
grafico_evolucao_expectativas_2026(df_expectativas_selic, df_comparacao_selic)