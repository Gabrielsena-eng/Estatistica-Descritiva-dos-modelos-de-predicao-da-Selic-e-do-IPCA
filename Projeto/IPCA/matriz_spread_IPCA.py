import pandas as pd
import seaborn as sns

from intervalos.tabela_intervalos import compilar_dados_IPCA

df_completo = compilar_dados_IPCA(9)

df_completo['Erro_Previsao'] = df_completo['IPCA_Media'] - df_completo['IPCA_Real']
df_completo.to_csv('df_intervalo_IPCA.csv', index=False)

tabela_erro = df_completo.pivot_table(
    index='DataReferencia', 
    columns='Mes_Expectativa', 
    values='Erro_Previsao'
)

# 3. Força a ordem cronológica exata das colunas
tabela_erro = tabela_erro[['Mes_5', 'Mes_3', 'Mes_1']]
tabela_erro.index = pd.to_datetime(tabela_erro.index).strftime('%Y-%m')

# 4. Aplica a estilização nativa do Pandas (Formatação Condicional)
# Vermelho = superestimou, Azul = subestimou.
tabela_estilizada = tabela_erro.style\
    .background_gradient(cmap='vlag', axis=None, vmin=-0.20, vmax=0.20)\
    .format("{:+.2f}")\
    .set_caption("Spread de Previsão do IPCA(Mercado vs Realidade)")\
    .set_table_styles([{
        'selector': 'caption',
        'props': [('font-size', '16px'), ('font-weight', 'bold'), ('color', '#1C1C1C'), ('margin-bottom', '10px')]
    }, {
        'selector': 'th',
        'props': [('background-color', '#1B3B6F'), ('color', 'white'), ('text-align', 'center'), ('padding', '10px')]
    }, {
        'selector': 'td',
        'props': [('text-align', 'center'), ('font-weight', 'bold'), ('padding', '10px'), ('border', '1px solid white')]
    }])


with open('matriz_erro_ipca.html', 'w', encoding='utf-8') as f:
    f.write(tabela_estilizada.to_html())