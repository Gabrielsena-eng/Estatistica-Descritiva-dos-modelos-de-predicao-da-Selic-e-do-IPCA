import matplotlib.pyplot as plt
import pandas as pd


from TabelaDeComparacao import df_comparacao_selic
from TabelaDeComparacao import df_comparacao_ipca


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
plotar_barras_comparacao(df_comparacao_selic, 'Teste')
