import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from TabelaDeComparacao import df_comparacao_selic
from TabelaDeComparacao import df_comparacao_ipca
from expectativas_IPCA import alinhar_dados_ipca
from expectativas_selic import extrair_dados_expectativa_selic
from expectativas_IPCA import extrair_dados_expectativa_ipca


def plotar_barras_comparacao(df, titulo):
   
    df['Data_str'] = df['Data'].dt.strftime('%Y-%m-%d')
    
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    
    df.plot(
        x='Data_str',
        y=['Valor_esperado', 'Valor_Real'],
        kind='bar',
        ax=ax,
        color=['#1f77b4', '#d62728'], 
        width=0.8
    )
    
    
    ax.set_title(titulo, fontsize=14, fontweight='bold')
    ax.set_ylabel('Taxa (%)', fontsize=12)
    ax.set_xlabel('Data', fontsize=12)
    
    plt.xticks(rotation=45, ha='right')
    plt.legend(['Expectativa (Mercado)', 'Realidade (BCB)'])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    
    plt.tight_layout()
    plt.show()

plotar_barras_comparacao(df_comparacao_ipca, 'Teste')


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