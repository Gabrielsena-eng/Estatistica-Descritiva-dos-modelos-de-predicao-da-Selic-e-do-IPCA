import sys
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

diretorio_projeto = Path(__file__).resolve().parent.parent
if str(diretorio_projeto) not in sys.path:
    sys.path.append(str(diretorio_projeto))

from intervalos.tabela_intervalos import compilar_dados_IPCA

df_completo = compilar_dados_IPCA(5)
df_completo['Erro_Previsao'] = df_completo['IPCA_Media'] - df_completo['IPCA_Real']


ordem_tempo = ['Mes_5', 'Mes_3', 'Mes_1'] 


plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")


sns.boxplot(
    data=df_completo, 
    x='Mes_Expectativa', 
    y='Erro_Previsao', 
    order=ordem_tempo, 
    palette='viridis',
    linewidth=1.5,
    showfliers=True 
)


plt.axhline(0, color='#A31621', linestyle='--', linewidth=2, label='Convergência Perfeita (Erro Zero)')

plt.title('Compressão da Incerteza: Distribuição do Erro de Previsão por Distância', fontsize=14, fontweight='bold')
plt.xlabel('Distância até a Reunião', fontsize=12)
plt.ylabel('Dispersão do Erro (Pontos Percentuais)', fontsize=12)

plt.legend()
plt.tight_layout()
plt.show()