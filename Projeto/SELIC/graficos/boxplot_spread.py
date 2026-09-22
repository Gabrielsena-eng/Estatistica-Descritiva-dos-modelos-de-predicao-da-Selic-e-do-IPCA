import sys
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

diretorio_projeto = Path(__file__).resolve().parent.parent
if str(diretorio_projeto) not in sys.path:
    sys.path.append(str(diretorio_projeto))

from tabelas.tabela_de_periodos import df_completo

# 1. Cálculo da magnitude do erro matemático (Spread)
df_completo['Erro_Previsao'] = df_completo['Media'] - df_completo['Selic_Real']

# 2. Ordem cronológica exata das colunas
ordem_tempo = ['Mes_5', 'Mes_3', 'Mes_1'] 

# Configuração visual
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# O Boxplot sem parâmetros de hue/legend para evitar qualquer bug interno de versão
sns.boxplot(
    data=df_completo, 
    x='Mes_Expectativa', 
    y='Erro_Previsao', 
    order=ordem_tempo, 
    palette='viridis',
    linewidth=1.5,
    showfliers=True 
)

# A linha do zero é o alvo absoluto
plt.axhline(0, color='#A31621', linestyle='--', linewidth=2, label='Convergência Perfeita (Erro Zero)')

rotulos_apresentacao = ['5 Meses Antes', '3 Meses Antes', '1 Mês Antes']
plt.xticks(ticks=range(len(ordem_tempo)), labels=rotulos_apresentacao, fontsize=11)

plt.title('Distribuição do Erro de Previsão do SELIC por Antecedência', fontsize=14, fontweight='bold')
plt.xlabel('Horizonte de Previsão', fontsize=12)
plt.ylabel('Erro de Previsão (Pontos Percentuais)', fontsize=12)

plt.legend()
plt.tight_layout()
plt.show()