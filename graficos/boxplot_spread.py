import matplotlib.pyplot as plt
import seaborn as sns

from Projeto.SELIC.tabelas.tabela_de_periodos import df_completo

# Garante a ordenação cronológica decrescente no eixo X
ordem_tempo = ['5 meses', '3 meses', '1 mês']

# Configuração visual
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# O Boxplot revela a mediana do erro, os quartis (onde estão 50% das previsões) e os outliers
sns.boxplot(
    data=df_completo, 
    x='Mes_Expectativa', 
    y='Erro_Previsao', 
    order=ordem_tempo, 
    palette='viridis',
    linewidth=1.5,
    showfliers=True # Mantém os pontos fora da curva para escancarar os piores erros
)

# A linha do zero é o alvo absoluto (acerto perfeito)
plt.axhline(0, color='#A31621', linestyle='--', linewidth=2, label='Convergência Perfeita (Erro Zero)')

plt.title('Compressão da Incerteza: Distribuição do Erro de Previsão por Distância', fontsize=14, fontweight='bold')
plt.xlabel('Distância até a Reunião', fontsize=12)
plt.ylabel('Dispersão do Erro (Pontos Percentuais)', fontsize=12)

plt.legend()
plt.tight_layout()
plt.show()